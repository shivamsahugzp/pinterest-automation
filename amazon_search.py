"""
Amazon Product Search and Affiliate Link Generation
Searches Amazon products and generates affiliate links
"""

import requests
import json
import hashlib
import hmac
import base64
from urllib.parse import quote_plus, urlencode
from datetime import datetime
from typing import Dict, List, Optional


class AmazonProductSearch:
    def __init__(self, config: dict):
        self.access_key = config.get('amazon', {}).get('access_key')
        self.secret_key = config.get('amazon', {}).get('secret_key')
        self.associate_tag = config.get('amazon', {}).get('associate_tag')
        self.marketplace = config.get('amazon', {}).get('marketplace', 'amazon.com')
        
    def search_product(self, query: str, item_page: int = 1) -> Optional[Dict]:
        """
        Search for products on Amazon using Product Advertising API
        Returns product details including images, price, and affiliate link
        """
        try:
            # For demo purposes, we'll create a mock product
            # In production, replace this with actual Amazon PA-API calls
            
            product = self._mock_product_search(query)
            
            if product:
                # Add affiliate link
                product['affiliate_link'] = self._generate_affiliate_link(product.get('asin', ''))
                product['images'] = product.get('images', [])
                
            return product
            
        except Exception as e:
            print(f"Error searching Amazon: {e}")
            return None
    
    def _generate_affiliate_link(self, asin: str) -> str:
        """Generate Amazon affiliate link"""
        if not asin:
            return ""
        
        base_url = f"https://www.amazon.com/dp/{asin}"
        affiliate_link = f"{base_url}/?tag={self.associate_tag}"
        return affiliate_link
    
    def get_product_details(self, asin: str) -> Optional[Dict]:
        """Get detailed product information from ASIN"""
        try:
            # Mock product details - replace with actual PA-API call in production
            product = self._mock_product_details(asin)
            
            if product:
                product['affiliate_link'] = self._generate_affiliate_link(asin)
            
            return product
            
        except Exception as e:
            print(f"Error getting product details: {e}")
            return None
    
    def find_alternative_product(self, original_query: str, ranking: int = 1) -> Optional[Dict]:
        """
        Find alternative products if main product not found
        ranking: 1 = second most popular, 2 = third most popular, etc.
        """
        try:
            # Search variations of the query
            variations = self._generate_query_variations(original_query, ranking)
            
            for variant in variations:
                product = self.search_product(variant)
                if product:
                    return product
            
            return None
            
        except Exception as e:
            print(f"Error finding alternative: {e}")
            return None
    
    def _generate_query_variations(self, query: str, ranking: int) -> List[str]:
        """Generate search query variations"""
        variations = [
            f"{query} best seller",
            f"best {query}",
            f"{query} popular",
            f"top rated {query}",
            f"{query} amazon choice"
        ]
        return variations[ranking:]
    
    def _mock_product_search(self, query: str) -> Optional[Dict]:
        """Mock Amazon product for testing (replace with real API)"""
        products = {
            'home decor': {
                'asin': 'B08XYZ1234',
                'title': 'Modern Wall Art Canvas Prints Set',
                'price': 29.99,
                'rating': 4.5,
                'reviews': 1523,
                'images': [
                    'https://m.media-amazon.com/images/I/71example1.jpg',
                    'https://m.media-amazon.com/images/I/71example2.jpg'
                ],
                'description': 'High quality canvas prints perfect for home decoration',
                'category': 'Home & Kitchen',
                'best_seller': True
            },
            'kitchen gadgets': {
                'asin': 'B09XYZ5678',
                'title': 'Smart Instant Pot Pressure Cooker',
                'price': 89.99,
                'rating': 4.7,
                'reviews': 3456,
                'images': [
                    'https://m.media-amazon.com/images/I/81example1.jpg',
                    'https://m.media-amazon.com/images/I/81example2.jpg'
                ],
                'description': '7-in-1 programmable pressure cooker with smart features',
                'category': 'Kitchen & Dining',
                'best_seller': True
            }
        }
        
        # Return matching product
        for key, product in products.items():
            if key.lower() in query.lower():
                return product
        
        # Default product
        return {
            'asin': f'B{hashlib.md5(query.encode()).hexdigest()[:9].upper()}',
            'title': f'Premium {query.title()}',
            'price': 39.99,
            'rating': 4.3,
            'reviews': 456,
            'images': ['https://via.placeholder.com/500x750?text=Product'],
            'description': f'High quality {query}',
            'category': 'General',
            'best_seller': False
        }
    
    def _mock_product_details(self, asin: str) -> Optional[Dict]:
        """Mock product details"""
        return self._mock_product_search('product')


def search_amazon_product(query: str, config: dict, fallback_rank: int = 0) -> Optional[Dict]:
    """
    Main function to search Amazon for a product
    Includes fallback logic if product not found
    """
    searcher = AmazonProductSearch(config)
    
    # Try primary search
    product = searcher.search_product(query)
    
    # If not found, try alternatives
    if not product and fallback_rank > 0:
        product = searcher.find_alternative_product(query, fallback_rank)
    
    if product:
        print(f"Found product: {product['title']} - ${product['price']}")
    
    return product


if __name__ == "__main__":
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Test search
    product = search_amazon_product('home decor', config)
    if product:
        print(json.dumps(product, indent=2))

