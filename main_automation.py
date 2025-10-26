"""
Main Pinterest-Amazon Automation Script
Coordinates research, product finding, image processing, and pin creation
"""

import json
import os
import time
import random
import schedule
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from pinterest_research import get_trending_products_on_pinterest
from amazon_search import search_amazon_product
from image_processor import optimize_image_for_pin
from pin_creator import prepare_pin_for_creation
from database import save_product, get_recently_posted
from scheduler import get_next_posting_time, is_time_to_post
from mcp_integration import create_pinterest_pin_via_mcp


class PinterestAmazonAutomation:
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the automation system"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.posts_today = 0
        self.max_posts_per_day = self.config.get('automation', {}).get('pins_per_day', 3)
        self.include_fallback = self.config.get('automation', {}).get('include_fallback', True)
        
    def research_and_post_cycle(self) -> bool:
        """
        Complete cycle: Research Pinterest → Find Amazon Product → Create Pin
        Returns True if successful
        """
        try:
            print(f"\n{'='*60}")
            print(f"Starting Pinterest-Amazon Automation Cycle - {datetime.now()}")
            print(f"{'='*60}\n")
            
            # Step 1: Research trending products on Pinterest
            print("📊 Step 1: Researching trending products on Pinterest...")
            trending_products = get_trending_products_on_pinterest(self.config)
            
            if not trending_products:
                print("❌ No trending products found")
                return False
            
            print(f"✅ Found {len(trending_products)} trending products")
            
            # Step 2: Select product to feature
            selected_product = self._select_best_product(trending_products)
            print(f"🎯 Selected: {selected_product.get('suggested_product', 'Unknown')}")
            
            # Step 3: Search for product on Amazon
            print("\n🔍 Step 2: Searching product on Amazon...")
            amazon_product = self._find_amazon_product(selected_product)
            
            if not amazon_product:
                print("❌ Product not found on Amazon")
                if self.include_fallback:
                    print("🔄 Trying fallback product...")
                    amazon_product = self._find_amazon_product(selected_product, fallback_rank=1)
            
            if not amazon_product:
                print("❌ Could not find product on Amazon")
                return False
            
            print(f"✅ Found: {amazon_product['title']} - ${amazon_product.get('price', 0)}")
            
            # Step 4: Process images
            print("\n🖼️  Step 3: Processing and optimizing images...")
            images = amazon_product.get('images', [])
            if not images:
                print("❌ No images available")
                return False
            
            optimized_image = self._process_product_image(images[0], amazon_product['title'])
            if not optimized_image:
                print("❌ Image processing failed")
                return False
            
            print(f"✅ Image ready: {optimized_image}")
            
            # Step 5: Create Pinterest pin
            print("\n📌 Step 4: Creating Pinterest pin...")
            success = self._create_pinterest_pin(amazon_product, optimized_image)
            
            if success:
                print("\n🎉 SUCCESS: Pin created and scheduled!")
                self.posts_today += 1
                
                # Save to database
                save_product(amazon_product, selected_product, success)
                
                return True
            else:
                print("\n❌ Failed to create pin")
                return False
                
        except Exception as e:
            print(f"\n❌ Error in automation cycle: {e}")
            import traceback
            traceback.print_exception(e)
            return False
    
    def _select_best_product(self, trending_products: List[Dict]) -> Dict:
        """Select the best product from trending list"""
        # Filter out recently posted products
        recently_posted_asins = get_recently_posted(days=7)
        
        available_products = [
            p for p in trending_products 
            if p.get('suggested_product') not in recently_posted_asins
        ]
        
        if not available_products:
            available_products = trending_products
        
        # Select top product
        return available_products[0]
    
    def _find_amazon_product(self, pinterest_product: Dict, fallback_rank: int = 0) -> Optional[Dict]:
        """Find product on Amazon"""
        query = pinterest_product.get('suggested_product') or pinterest_product.get('keyword', '')
        return search_amazon_product(query, self.config, fallback_rank)
    
    def _process_product_image(self, image_url: str, product_title: str) -> Optional[str]:
        """Process and optimize product image"""
        return optimize_image_for_pin(image_url, product_title, self.config)
    
    def _create_pinterest_pin(self, product: Dict, image_path: str) -> bool:
        """
        Create Pinterest pin via MCP API
        Returns True if successful
        """
        try:
            # Prepare pin data
            pin_data = prepare_pin_for_creation(product, image_path, self.config)
            
            # Get board ID (should be retrieved from Pinterest)
            board_name = self.config.get('board_settings', {}).get('boards', ['Amazon Finds'])[0]
            
            print(f"📋 Pin Data:")
            print(f"   Title: {pin_data['title']}")
            print(f"   Description: {pin_data['description'][:100]}...")
            print(f"   Board: {board_name}")
            print(f"   Link: {product.get('affiliate_link', 'N/A')}")
            
            # Create pin via MCP
            print("\n🚀 Creating pin via MCP...")
            success = create_pinterest_pin_via_mcp(
                board_name=board_name,
                image_path=image_path,
                title=pin_data['title'],
                description=pin_data['description'],
                link=product.get('affiliate_link', '')
            )
            
            if success:
                print("\n✅ Pin created successfully via MCP!")
            else:
                print("\n❌ Failed to create pin via MCP")
            
            return success
            
        except Exception as e:
            print(f"Error creating pin: {e}")
            return False
    
    def should_post_today(self) -> bool:
        """Check if we should post today based on limits"""
        return self.posts_today < self.max_posts_per_day
    
    def run_scheduled_automation(self):
        """Run automation at scheduled times"""
        print(f"⏰ Running scheduled automation at {datetime.now()}")
        
        if not self.should_post_today():
            print(f"ℹ️  Daily limit reached ({self.posts_today}/{self.max_posts_per_day})")
            return
        
        self.research_and_post_cycle()
    
    def start_daily_schedule(self):
        """Start the daily automation schedule"""
        print("\n🚀 Starting Pinterest-Amazon Automation System")
        print(f"📅 Daily posting limit: {self.max_posts_per_day} pins")
        print(f"⏰ Random time range: ±{self.config.get('automation', {}).get('random_time_range', 30)} minutes\n")
        
        # Schedule posts at configured times
        post_times = self.config.get('automation', {}).get('post_times', [])
        
        for time_config in post_times:
            hour = time_config['hour']
            minute = time_config['minute']
            schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(self.run_scheduled_automation)
            print(f"✅ Scheduled post at {hour:02d}:{minute:02d}")
        
        print("\n⏳ Waiting for scheduled times...\n")
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute


def main():
    """Main entry point"""
    automation = PinterestAmazonAutomation()
    
    # Check if running on demand or scheduled
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        # Run immediately
        automation.research_and_post_cycle()
    else:
        # Run with schedule
        automation.start_daily_schedule()


if __name__ == "__main__":
    main()

