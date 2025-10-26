"""
Database Module for Tracking Posted Products
Stores product details to avoid duplicates
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict


class ProductDatabase:
    def __init__(self, db_path: str = 'posted_products.json'):
        self.db_path = db_path
        self.data = self._load_database()
    
    def _load_database(self) -> dict:
        """Load database from file"""
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading database: {e}")
                return {'products': []}
        return {'products': []}
    
    def _save_database(self):
        """Save database to file"""
        try:
            with open(self.db_path, 'w') as f:
                json.dump(self.data, f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving database: {e}")
    
    def save_product(self, product: Dict, pinterest_data: Dict, pin_created: bool):
        """Save product to database"""
        entry = {
            'asin': product.get('asin'),
            'title': product.get('title'),
            'price': product.get('price'),
            'affiliate_link': product.get('affiliate_link'),
            'pinterest_keyword': pinterest_data.get('keyword'),
            'posted_at': datetime.now().isoformat(),
            'pin_created': pin_created
        }
        
        self.data.setdefault('products', []).append(entry)
        self._save_database()
    
    def get_recently_posted(self, days: int = 7) -> List[str]:
        """Get list of ASINs posted in last N days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        recent = []
        for product in self.data.get('products', []):
            posted_at = product.get('posted_at')
            if posted_at:
                try:
                    posted_date = datetime.fromisoformat(posted_at)
                    if posted_date >= cutoff_date:
                        recent.append(product.get('asin'))
                except:
                    pass
        
        return recent
    
    def get_product_stats(self) -> Dict:
        """Get statistics about posted products"""
        products = self.data.get('products', [])
        
        stats = {
            'total': len(products),
            'successful': len([p for p in products if p.get('pin_created', False)]),
            'failed': len([p for p in products if not p.get('pin_created', False)]),
            'last_7_days': len(self.get_recently_posted(7)),
            'last_30_days': len(self.get_recently_posted(30))
        }
        
        return stats


# Global instance
_db_instance = None

def get_db() -> ProductDatabase:
    """Get database instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = ProductDatabase()
    return _db_instance

def save_product(product: Dict, pinterest_data: Dict, pin_created: bool):
    """Save product to database"""
    db = get_db()
    db.save_product(product, pinterest_data, pin_created)

def get_recently_posted(days: int = 7) -> List[str]:
    """Get recently posted ASINs"""
    db = get_db()
    return db.get_recently_posted(days)

def get_stats() -> Dict:
    """Get product statistics"""
    db = get_db()
    return db.get_product_stats()


if __name__ == "__main__":
    # Test database
    stats = get_stats()
    print(f"Database stats: {stats}")
    
    # Test save
    test_product = {'asin': 'B123456', 'title': 'Test Product'}
    test_pinterest = {'keyword': 'test'}
    save_product(test_product, test_pinterest, True)
    
    print(f"Updated stats: {get_stats()}")

