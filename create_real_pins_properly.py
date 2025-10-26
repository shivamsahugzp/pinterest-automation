#!/usr/bin/env python3
"""
Create Pinterest pins with REAL Amazon products
Uses actual Amazon product data with real images and descriptions
"""

import json
import random

# Real Amazon products with working affiliate links
# These are actual products with real images and descriptions
REAL_AMAZON_PRODUCTS = [
    {
        "keyword": "smart speaker",
        "title": "Echo Dot (5th Gen) | Smart speaker with Alexa",
        "description": "Our most popular smart speaker - Now with improved sound and a new design. Voice control your music, check weather, control smart home devices, and more hands-free with Alexa.",
        "price": "$29.99",
        "rating": "4.6",
        "images": [
            "https://m.media-amazon.com/images/I/714Rq4k05UL._AC_SL1000_.jpg"
        ],
        "amazon_url": "https://www.amazon.com/dp/B09B8V1LZ3",
        "associate_tag": "shivamsahu010-21"
    },
    {
        "keyword": "wireless earbuds", 
        "title": "Apple AirPods Pro (2nd Generation) - Active Noise Cancelling",
        "description": "Active Noise Cancellation eliminates outside noise, while Adaptive Transparency lets outside sounds in. Personalized Spatial Audio with dynamic head tracking places sound all around you.",
        "price": "$249.00",
        "rating": "4.5",
        "images": [
            "https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_SL1500_.jpg"
        ],
        "amazon_url": "https://www.amazon.com/dp/B0BDHB9Y8H",
        "associate_tag": "shivamsahu010-21"
    },
    {
        "keyword": "laptop stand",
        "title": "Rain Design mStand Laptop Stand - Space Gray",
        "description": "The mStand elevates your laptop to eye level, improving posture and reducing neck strain. Solid aluminum construction with ergonomic design. Fits most laptops up to 15 inches.",
        "price": "$59.95",
        "rating": "4.7",
        "images": [
            "https://m.media-amazon.com/images/I/71h8yvTXcPL._AC_SL1500_.jpg"
        ],
        "amazon_url": "https://www.amazon.com/dp/B002OOZYE4",
        "associate_tag": "shivamsahu010-21"
    },
    {
        "keyword": "desk lamp",
        "title": "BenQ e-Reading LED Desk Lamp | Eye-Care Technology",
        "description": "Asymmetric light design reduces screen glare. 15 brightness levels with even illumination. Flexible gooseneck for optimal positioning. Built-in ambient light sensor.",
        "price": "$189.00",
        "rating": "4.5",
        "images": [
            "https://m.media-amazon.com/images/I/81V+Ls5H0NL._AC_SL1500_.jpg"
        ],
        "amazon_url": "https://www.amazon.com/dp/B0196M1CLO",
        "associate_tag": "shivamsahu010-21"
    },
    {
        "keyword": "phone case",
        "title": "OtterBox Defender Series Phone Case for iPhone",
        "description": "Triple-layer defense with port protection. Drop tested and certified for MIL-STD-810G. Includes belt-clip holster with carabiner. Lifetime warranty.",
        "price": "$44.95",
        "rating": "4.4",
        "images": [
            "https://m.media-amazon.com/images/I/815GpCbMGhL._AC_SL1500_.jpg"
        ],
        "amazon_url": "https://www.amazon.com/dp/B08N5C8HJZ",
        "associate_tag": "shivamsahu010-21"
    }
]


def create_affiliate_link(amazon_url, associate_tag):
    """Create proper Amazon affiliate link with associate tag"""
    if "?" in amazon_url:
        if "tag=" in amazon_url:
            # Replace existing tag
            base_url = amazon_url.split("?")[0]
            params = amazon_url.split("?")[1]
            param_dict = dict(item.split("=") for item in params.split("&") if "=" in item)
            param_dict["tag"] = associate_tag
            return base_url + "?" + "&".join([f"{k}={v}" for k, v in param_dict.items()])
        else:
            return f"{amazon_url}&tag={associate_tag}"
    else:
        return f"{amazon_url}?tag={associate_tag}"


def prepare_pin_data(product):
    """Prepare pin data with proper formatting"""
    affiliate_link = create_affiliate_link(product['amazon_url'], product['associate_tag'])
    
    # Create engaging pin description
    description = f"{product['description']}\n\n💰 Price: {product['price']}\n⭐ Rating: {product['rating']}/5\n\n🛒 Buy now: Click the link above!\n\n#AmazonFinds #BestProducts #MustHave #TechDeals #ShoppingDeals"
    
    return {
        'title': product['title'],
        'description': description,
        'image_url': product['images'][0],
        'link': affiliate_link
    }


def create_pins_today(num_pins=3):
    """Create pins for today with real Amazon products"""
    
    print(f"\n{'='*60}")
    print(f"🚀 Creating {num_pins} Pins with REAL Amazon Products")
    print(f"{'='*60}\n")
    
    # Select random products
    selected_products = random.sample(REAL_AMAZON_PRODUCTS, min(num_pins, len(REAL_AMAZON_PRODUCTS)))
    
    for i, product in enumerate(selected_products, 1):
        print(f"📌 Preparing Pin {i}/{len(selected_products)}")
        print(f"   Product: {product['title']}")
        
        pin_data = prepare_pin_data(product)
        
        print(f"   Image: {pin_data['image_url'][:80]}...")
        print(f"   Link: {pin_data['link'][:80]}...")
        print()
    
    print(f"✅ Prepared {len(selected_products)} pins with real Amazon products!")
    
    return [prepare_pin_data(p) for p in selected_products]


if __name__ == "__main__":
    pins = create_pins_today(3)
    print("\nPins ready to create:")
    for i, pin in enumerate(pins, 1):
        print(f"\n{i}. {pin['title']}")
        print(f"   Link: {pin['link']}")

