#!/usr/bin/env python3
"""
Daily Automated Pinterest Pin Creation
Posts 10 pins throughout the day automatically
"""

import json
import random
import time
from datetime import datetime
import schedule
import os

# Load configuration
CONFIG_FILE = 'config.json'
BATCH_CONFIG_FILE = 'batch_posting_times.json'

# Most searched products (same as before)
MOST_SEARCHED_PRODUCTS = [
    {
        "title": "Modern Abstract Wall Art Canvas Prints - Set of 3",
        "amazon_asin": "B0B5JZWX5K",
        "description": "Minimalist abstract canvas prints perfect for modern home decor. High quality UV print on canvas. 3-piece set.",
        "price": "$29.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/81xBjCsaF6L._AC_SL1500_.jpg",
        "hashtags": "#HomeDecor #WallArt #Minimalist"
    },
    {
        "title": "Instant Pot Duo 7-in-1 Electric Pressure Cooker - 6 Qt",
        "amazon_asin": "B01B1VC13K",
        "description": "Pressure cooker, slow cooker, rice cooker, steamer in one! Cooks 70% faster. Over 1000 5-star ratings.",
        "price": "$99.00",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/71WOl-vQKpL._AC_SL1500_.jpg",
        "hashtags": "#Kitchen #Cooking #InstantPot"
    },
    {
        "title": "Premium Exercise Yoga Mat with Carrying Strap",
        "amazon_asin": "B07JMHR5PF",
        "description": "Extra thick non-slip yoga mat. Lightweight with carrying strap. Perfect for yoga and fitness. Eco-friendly material.",
        "price": "$24.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/61v5YbJVp+L._AC_SL1500_.jpg",
        "hashtags": "#Fitness #Yoga #Exercise"
    },
    {
        "title": "Complete Daily Skincare Routine Kit - 5 Piece Set",
        "amazon_asin": "B0C3VDF8Q1",
        "description": "Complete skincare set with cleanser, toner, serum, moisturizer and sunscreen. Dermatologist tested.",
        "price": "$39.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71Kpjb-HiGL._AC_SL1500_.jpg",
        "hashtags": "#Beauty #Skincare #SelfCare"
    },
    {
        "title": "Wireless Earbuds - Bluetooth 5.0 with Noise Cancellation",
        "amazon_asin": "B08XYZ1234",
        "description": "Premium wireless earbuds with active noise cancellation. 30-hour battery life. IPX7 waterproof.",
        "price": "$59.99",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_SL1500_.jpg",
        "hashtags": "#Tech #WirelessEarbuds"
    },
    {
        "title": "Clear Plastic Storage Bins with Lids - 6 Pack",
        "amazon_asin": "B08N5C8HJ1",
        "description": "Stackable clear storage bins for organizing closet, pantry, and garage. Heavy duty plastic with secure lids.",
        "price": "$34.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/81YH6V3i8+L._AC_SL1500_.jpg",
        "hashtags": "#Organization #Storage"
    },
    {
        "title": "Adjustable Standing Desk Converter - 35.4\" Wide",
        "amazon_asin": "B09KL7N2X4",
        "description": "Height adjustable standing desk converter. Ergonomic design reduces neck and back pain. Fits dual monitors.",
        "price": "$149.00",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71Nwz0jFkBL._AC_SL1500_.jpg",
        "hashtags": "#Office #StandingDesk #WFH"
    },
    {
        "title": "Ninja AF101 Air Fryer - 4 Quart Capacity",
        "amazon_asin": "B07GJBBLGL",
        "description": "Delivers 75% less fat than traditional frying. Cooks 75% faster with little to no oil. 1550W cooking power.",
        "price": "$89.99",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/71NCKMomP1L._AC_SL1500_.jpg",
        "hashtags": "#Kitchen #AirFryer #Healthy"
    },
    {
        "title": "Stainless Steel Water Bottle - 32oz Insulated",
        "amazon_asin": "B07CZDQ6VZ",
        "description": "Double wall insulated keeps drinks cold 24 hours or hot 12 hours. Leak-proof design. Wide mouth. BPA-free.",
        "price": "$24.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71LgcGpzVYL._AC_SL1500_.jpg",
        "hashtags": "#Fitness #WaterBottle #Healthy"
    },
    {
        "title": "Smart LED Light Bulbs - 4 Pack with Alexa/Google Home",
        "amazon_asin": "B08YPZH81J",
        "description": "Voice control with Alexa and Google Assistant. 16 million colors, adjustable brightness. Energy efficient LED.",
        "price": "$29.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/71FZ+gN6FrL._AC_SL1500_.jpg",
        "hashtags": "#SmartHome #LEDLights #Tech"
    }
]

# Plus 20 more products for variety
ADDITIONAL_PRODUCTS = [
    {"title": "Apple AirPods Pro (2nd Gen)", "amazon_asin": "B0BDHB9Y8H", "price": "$249.00", "rating": "4.5"},
    {"title": "Ring Video Doorbell", "amazon_asin": "B09N3T1FNK", "price": "$99.99", "rating": "4.5"},
    {"title": "Nespresso Coffee Maker", "amazon_asin": "B07VNQ42QX", "price": "$149.00", "rating": "4.7"},
    {"title": "Kindle Paperwhite", "amazon_asin": "B08KTZ8249", "price": "$139.99", "rating": "4.8"},
    {"title": "Portable Phone Charger", "amazon_asin": "B08XYZ1235", "price": "$19.99", "rating": "4.6"},
    {"title": "Laptop Stand", "amazon_asin": "B08N5C8HJ2", "price": "$49.99", "rating": "4.7"},
    {"title": "Memory Foam Mattress", "amazon_asin": "B07BY2Y81D", "price": "$199.00", "rating": "4.6"},
    {"title": "Robot Vacuum", "amazon_asin": "B08XYZ1236", "price": "$229.99", "rating": "4.5"},
    {"title": "Noise Cancelling Headphones", "amazon_asin": "B07XRC2FMM", "price": "$179.99", "rating": "4.7"},
    {"title": "Adjustable Dumbbells", "amazon_asin": "B08N5C8HJ3", "price": "$299.00", "rating": "4.6"},
]


def load_config():
    """Load configuration from file"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        # Default config
        return {
            "associate_tag": "shivamsahu010-21",
            "board_name": "MCP Test Board",
            "posts_per_day": 10
        }


def create_affiliate_link(asin, associate_tag):
    """Create Amazon affiliate link"""
    return f"https://www.amazon.com/dp/{asin}?tag={associate_tag}"


def create_pin_description(product):
    """Create pin description with all details"""
    return f"{product['description']}\n\n💰 Price: {product['price']}\n⭐ Rating: {product['rating']}/5\n\n🛒 Click to buy on Amazon!\n\n{product['hashtags']} #AmazonFinds #BestProducts #MustHave #ShoppingDeals"


def post_single_pin(product, config, board_name):
    """Post a single pin to Pinterest"""
    try:
        from mcp_integration import create_pinterest_pin_via_mcp
        
        affiliate_link = create_affiliate_link(product['amazon_asin'], config['associate_tag'])
        description = create_pin_description(product)
        
        print(f"\n📌 Posting: {product['title'][:50]}...")
        print(f"   Board: {board_name}")
        print(f"   Time: {datetime.now().strftime('%H:%M:%S')}")
        
        # Try to post via MCP (if available)
        success = create_pinterest_pin_via_mcp(
            board_name=board_name,
            image_path=product['image_url'],
            title=product['title'],
            description=description,
            link=affiliate_link
        )
        
        if success:
            print(f"   ✅ Pin posted successfully!")
        else:
            print(f"   ⚠️ MCP server issue - pin data prepared but not posted")
        
        return success
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def get_daily_posting_schedule():
    """Get times throughout the day to post pins"""
    return [
        {"hour": 8, "minute": 30},   # Morning
        {"hour": 9, "minute": 15},   # Morning
        {"hour": 11, "minute": 0},   # Late morning
        {"hour": 12, "minute": 45},  # Lunch time
        {"hour": 14, "minute": 30},  # Afternoon
        {"hour": 15, "minute": 45},  # Afternoon
        {"hour": 17, "minute": 15},  # Evening
        {"hour": 18, "minute": 45},  # Evening
        {"hour": 20, "minute": 30},  # Night
        {"hour": 21, "minute": 15},  # Night
    ]


def run_daily_pin_batch():
    """Run a batch of pins for the day"""
    config = load_config()
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting Daily Pinterest Automation")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"{'='*60}\n")
    
    # Select random products
    all_products = MOST_SEARCHED_PRODUCTS + ADDITIONAL_PRODUCTS
    daily_products = random.sample(all_products, config.get('posts_per_day', 10))
    
    board_name = config.get('board_name', 'MCP Test Board')
    
    for i, product in enumerate(daily_products, 1):
        print(f"\n[{i}/{len(daily_products)}] Posting pin...")
        post_single_pin(product, config, board_name)
        time.sleep(2)  # Small delay between posts
    
    print(f"\n{'='*60}")
    print(f"✅ Daily automation complete!")
    print(f"{'='*60}\n")


def schedule_daily_posts():
    """Schedule posts at specific times throughout the day"""
    config = load_config()
    posts_per_day = config.get('posts_per_day', 10)
    
    # Get posting times
    posting_times = get_daily_posting_schedule()[:posts_per_day]
    
    for time_config in posting_times:
        hour = time_config['hour']
        minute = time_config['minute']
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(run_single_pin_post)
    
    print(f"✅ Scheduled {posts_per_day} pins per day")
    for time_config in posting_times:
        print(f"   {time_config['hour']:02d}:{time_config['minute']:02d}")


def run_single_pin_post():
    """Post a single pin at scheduled time"""
    config = load_config()
    all_products = MOST_SEARCHED_PRODUCTS + ADDITIONAL_PRODUCTS
    product = random.choice(all_products)
    board_name = config.get('board_name', 'MCP Test Board')
    
    print(f"\n⏰ Scheduled pin posting at {datetime.now().strftime('%H:%M:%S')}")
    post_single_pin(product, config, board_name)


def main():
    """Main function"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--schedule':
        # Run with scheduler
        print("🔄 Starting scheduled pin posting system...")
        schedule_daily_posts()
        schedule.run_pending()
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)
    
    else:
        # Run once now
        print("🚀 Running daily pin batch...")
        run_daily_pin_batch()


if __name__ == "__main__":
    main()

