#!/usr/bin/env python3
"""
Get REAL Amazon product data including actual images and descriptions
Uses Amazon Product Advertising API or scraping
"""

import requests
from bs4 import BeautifulSoup
import json


def get_amazon_product_data(product_url):
    """
    Scrape Amazon product page to get real data
    Returns: title, price, images, description, etc.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(product_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get product title
        title_elem = soup.select_one('#productTitle')
        title = title_elem.get_text(strip=True) if title_elem else ""
        
        # Get price
        price_elem = soup.select_one('.a-price .a-offscreen, .a-price-whole')
        price = price_elem.get_text(strip=True) if price_elem else ""
        
        # Get product images
        images = []
        img_elements = soup.select('#landingImage, #imgBlkFront')
        for img in img_elem ents[:5]:  # Get first 5 images
            src = img.get('src') or img.get('data-src')
            if src and src.startswith('http'):
                images.append(src)
        
        # Get product description
        feature_bullets = soup.select('#feature-bullets li span')
        description = "\n".join([li.get_text(strip=True) for li in feature_bullets[1:6]])
        
        # Get rating
        rating_elem = soup.select_one('.a-icon-alt')
        rating = rating_elem.get_text(strip=True).split()[0] if rating_elem else ""
        
        # Get ASIN
        asin = soup.select_one('input[name="ASIN"]')
        asin_value = asin.get('value') if asin else ""
        
        return {
            'title': title,
            'price': price,
            'images': images,
            'description': description,
            'rating': rating,
            'asin': asin_value,
            'url': product_url
        }
        
    except Exception as e:
        print(f"Error getting Amazon data: {e}")
        return None


def search_amazon_trending_product(keyword):
    """
    Search for a trending product on Amazon and return the top result
    """
    search_url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first product result
        result = soup.select_one('[data-component-type="s-search-result"]')
        
        if result:
            # Get product URL
            link_elem = result.select_one('h2 a.a-link-normal')
            if link_elem:
                product_path = link_elem.get('href')
                if product_path and 'www.amazon.com' not in product_path:
                    product_url = f"https://www.amazon.com{product_path}"
                    return product_url
        
        return None
        
    except Exception as e:
        print(f"Error searching Amazon: {e}")
        return None


def create_affiliate_link(amazon_url, associate_tag="sahushivamgzp-20"):
    """
    Create proper Amazon affiliate link
    """
    if '?' in amazon_url:
        return f"{amazon_url}&tag={associate_tag}"
    else:
        return f"{amazon_url}?tag={associate_tag}"


def get_real_product_for_pin(keyword):
    """
    Get a complete real Amazon product for creating a pin
    """
    print(f"🔍 Searching Amazon for: {keyword}")
    
    # Search for product
    product_url = search_amazon_trending_product(keyword)
    
    if not product_url:
        print(f"❌ No product found for {keyword}")
        return None
    
    print(f"✅ Found product: {product_url}")
    
    # Get product details
    product_data = get_amazon_product_data(product_url)
    
    if not product_data:
        print(f"❌ Could not get product details")
        return None
    
    # Add affiliate link
    product_data['affiliate_link'] = create_affiliate_link(product_url, "sahushivamgzp-20")
    
    print(f"📦 Product: {product_data['title']}")
    print(f"💰 Price: {product_data['price']}")
    print(f"⭐ Rating: {product_data['rating']}")
    print(f"🖼️  Images: {len(product_data['images'])} found")
    
    return product_data


if __name__ == "__main__":
    # Test with a real keyword
    keyword = "wireless keyboard"
    product = get_real_product_for_pin(keyword)
    
    if product:
        print("\n" + "="*60)
        print("Product Data:")
        print("="*60)
        print(json.dumps(product, indent=2))

