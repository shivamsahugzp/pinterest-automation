"""
Pinterest Pin Creator Module
Creates pins with product details and affiliate links
"""

from typing import Dict, Optional
import json


class PinCreator:
    def __init__(self, config: dict):
        self.config = config
        
    def create_pin_description(self, product: Dict, category: str = None) -> str:
        """
        Create an engaging Pinterest description for the product
        Includes hashtags and call-to-action
        """
        title = product.get('title', 'Amazing Product')
        price = product.get('price', 0)
        rating = product.get('rating', 0)
        description = product.get('description', '')
        
        # Create description
        pin_text = f"{title}"
        
        if description:
            pin_text += f"\n\n{description}"
        
        # Add price and rating if available
        if price:
            pin_text += f"\n💰 Price: ${price}"
        
        if rating >= 4.0:
            pin_text += f"\n⭐ Rating: {rating}/5"
        
        # Add affiliate link note
        pin_text += "\n\n🛒 Click link to buy on Amazon!"
        
        # Add category and hashtags
        if category:
            pin_text += f"\n\n#{category.replace(' ', '')}"
        
        # Add popular hashtags
        hashtags = ["AmazonFinds", "BestProducts", "MustHave", "GiftIdeas", "ShoppingDeals"]
        for tag in hashtags[:3]:
            pin_text += f" #{tag}"
        
        return pin_text
    
    def create_pin_data(self, product: Dict, image_path: str, board_name: str = "Amazon Finds") -> Dict:
        """
        Create complete pin data structure
        Returns data ready to be posted via Pinterest API
        """
        pin_data = {
            'board_id': None,  # Will be set by caller
            'title': product.get('title', 'Product'),
            'description': self.create_pin_description(product, product.get('category', '')),
            'link': product.get('affiliate_link', ''),
            'media_source': {
                'source_type': 'image_url',
                'url': image_path  # In production, upload to Pinterest media
            },
            'product_details': {
                'price': product.get('price'),
                'currency': 'USD',
                'availability': 'in stock'
            }
        }
        
        return pin_data
    
    def format_affiliate_link(self, product: Dict) -> str:
        """
        Format affiliate link with UTM parameters for tracking
        """
        affiliate_link = product.get('affiliate_link', '')
        
        if not affiliate_link:
            return affiliate_link
        
        # Add UTM parameters
        utm_params = {
            'utm_source': 'pinterest',
            'utm_medium': 'pin',
            'utm_campaign': 'amazon_automation',
            'utm_content': product.get('asin', '')
        }
        
        # Add parameters to link
        separator = '&' if '?' in affiliate_link else '?'
        tracked_link = f"{affiliate_link}{separator}{'&'.join([f'{k}={v}' for k, v in utm_params.items()])}"
        
        return tracked_link
    
    def create_engaging_title(self, product: Dict) -> str:
        """Create an engaging pin title"""
        title = product.get('title', 'Product')
        
        # Add emoji and modifier
        best_seller = product.get('best_seller', False)
        
        if best_seller:
            return f"🔥 {title} - Amazon Best Seller!"
        else:
            return f"✨ {title}"
    
    def create_product_pin(self, product: Dict, image_path: str, config: dict) -> Dict:
        """
        Main function to create complete pin data for a product
        """
        # Get board settings
        boards = config.get('board_settings', {}).get('boards', ['Amazon Finds'])
        board_name = boards[0]  # Use first board
        
        # Format affiliate link
        product['affiliate_link'] = self.format_affiliate_link(product)
        
        # Create engaging title
        product['title'] = self.create_engaging_title(product)
        
        # Create pin data
        pin_data = self.create_pin_data(product, image_path, board_name)
        
        return pin_data


def prepare_pin_for_creation(product: Dict, image_path: str, config: dict) -> Dict:
    """
    Main function to prepare pin data for Pinterest
    """
    creator = PinCreator(config)
    return creator.create_product_pin(product, image_path, config)


if __name__ == "__main__":
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Test pin creation
    test_product = {
        'title': 'Smart Home Camera',
        'price': 49.99,
        'rating': 4.5,
        'description': 'WiFi security camera with night vision',
        'affiliate_link': 'https://amazon.com/dp/B123456',
        'best_seller': True,
        'category': 'Home Security'
    }
    
    pin_data = prepare_pin_for_creation(test_product, 'test_image.jpg', config)
    print(json.dumps(pin_data, indent=2))

