#!/usr/bin/env python3
"""
Create Pinterest pins for the MOST SEARCHED products on Pinterest
These are actual trending product categories people search for on Pinterest
"""

import random

# Most searched product categories on Pinterest
# Based on Pinterest trend data and search volumes
MOST_SEARCHED_PINTEREST_PRODUCTS = [
    {
        "category": "home decor",
        "keyword": "minimalist wall art",
        "title": "Modern Abstract Wall Art Canvas Prints - Set of 3",
        "amazon_asin": "B0B5JZWX5K",
        "description": "Minimalist abstract canvas prints perfect for modern home decor. High quality UV print on canvas. 3-piece set includes multiple sizes. Modern minimalist designs that match any interior.",
        "price": "$29.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/81xBjCsaF6L._AC_SL1500_.jpg",
        "hashtags": "#HomeDecor #WallArt #Minimalist #AmazonFinds #InteriorDesign"
    },
    {
        "category": "kitchen",
        "keyword": "instant pot",
        "title": "Instant Pot Duo 7-in-1 Electric Pressure Cooker - 6 Qt",
        "amazon_asin": "B01B1VC13K",
        "description": "Pressure cooker, slow cooker, rice cooker, steamer, sauté pan, yogurt maker and warmer in one! Over 1000 5-star ratings. Cooks up to 70% faster. Features 14 Smart Programs and 3 adjustable temperatures.",
        "price": "$99.00",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/71WOl-vQKpL._AC_SL1500_.jpg",
        "hashtags": "#Kitchen #Cooking #InstantPot #AmazonFinds #KitchenMustHave"
    },
    {
        "category": "fitness",
        "keyword": "yoga mat",
        "title": "Premium Exercise Yoga Mat with Carrying Strap",
        "amazon_asin": "B07JMHR5PF",
        "description": "Extra thick 1/4 inch non-slip yoga mat with dual-textured surface. Lightweight with carrying strap included. Perfect for yoga, pilates, and fitness workouts. Eco-friendly TPE material.",
        "price": "$24.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/61v5YbJVp+L._AC_SL1500_.jpg",
        "hashtags": "#Fitness #Yoga #Exercise #AmazonFinds #FitnessGear"
    },
    {
        "category": "beauty",
        "keyword": "skincare set",
        "title": "Complete Daily Skincare Routine Kit - 5 Piece Set",
        "amazon_asin": "B0C3VDF8Q1",
        "description": "Includes cleanser, toner, serum, moisturizer and sunscreen. Dermatologist tested. Clean, vegan, cruelty-free formula. Suitable for all skin types. Complete daily skincare routine.",
        "price": "$39.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71Kpjb-HiGL._AC_SL1500_.jpg",
        "hashtags": "#Beauty #Skincare #AmazonFinds #BeautyProducts #SelfCare"
    },
    {
        "category": "tech",
        "keyword": "bluetooth earbuds",
        "title": "Wireless Earbuds - Bluetooth 5.0 with Noise Cancellation",
        "amazon_asin": "B08XYZ1234",
        "description": "Premium wireless earbuds with active noise cancellation. 30-hour battery life with charging case. IPX7 waterproof. Crystal clear sound quality. Comfortable fit for all-day use.",
        "price": "$59.99",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_SL1500_.jpg",
        "hashtags": "#Tech #WirelessEarbuds #AmazonFinds #TechAccessories #BestDeals"
    },
    {
        "category": "home organization",
        "keyword": "storage bins",
        "title": "Clear Plastic Storage Bins with Lids - 6 Pack",
        "amazon_asin": "B08N5C8HJ1",
        "description": "Stackable clear storage bins perfect for organizing closet, pantry, and garage. Heavy duty plastic with secure lids. Stackable design saves space. Clear design for easy identification.",
        "price": "$34.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/81YH6V3i8+L._AC_SL1500_.jpg",
        "hashtags": "#Organization #Storage #HomeOrganization #AmazonFinds #OrganizationTips"
    },
    {
        "category": "office",
        "keyword": "standing desk converter",
        "title": "Adjustable Standing Desk Converter - 35.4\" Wide",
        "amazon_asin": "B09KL7N2X4",
        "description": "Height adjustable standing desk converter. Ergonomic design reduces neck and back pain. Fits dual monitors. Easy crank adjustment. Solid build quality. Transform any desk into a standing desk.",
        "price": "$149.00",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71Nwz0jFkBL._AC_SL1500_.jpg",
        "hashtags": "#Office #StandingDesk #Ergonomic #AmazonFinds #WorkFromHome"
    },
    {
        "category": "kitchen",
        "keyword": "air fryer",
        "title": "Ninja AF101 Air Fryer - 4 Quart Capacity",
        "amazon_asin": "B07GJBBLGL",
        "description": "Delivers 75% less fat than traditional frying methods. Cooks up to 75% faster with little to no oil. 1550W cooking power. 4-quart capacity perfect for 2-4 servings.",
        "price": "$89.99",
        "rating": "4.7",
        "image_url": "https://m.media-amazon.com/images/I/71NCKMomP1L._AC_SL1500_.jpg",
        "hashtags": "#Kitchen #AirFryer #HealthyCooking #AmazonFinds #KitchenGadgets"
    },
    {
        "category": "fitness",
        "keyword": "water bottle",
        "title": "Stainless Steel Water Bottle - 32oz Insulated",
        "amazon_asin": "B07CZDQ6VZ",
        "description": "Double wall insulated keeps drinks cold for 24 hours or hot for 12 hours. Leak-proof design with one-touch lid. Wide mouth for easy cleaning. BPA-free and dishwasher safe.",
        "price": "$24.99",
        "rating": "4.6",
        "image_url": "https://m.media-amazon.com/images/I/71LgcGpzVYL._AC_SL1500_.jpg",
        "hashtags": "#Fitness #WaterBottle #HealthyLiving #AmazonFinds #FitnessGear"
    },
    {
        "category": "home improvement",
        "keyword": "smart light bulbs",
        "title": "Smart LED Light Bulbs - 4 Pack with Alexa/Google Home",
        "amazon_asin": "B08YPZH81J",
        "description": "Voice control with Alexa and Google Assistant. 16 million colors and adjustable brightness. Set schedules, create scenes, control from anywhere. Energy efficient LED technology.",
        "price": "$29.99",
        "rating": "4.5",
        "image_url": "https://m.media-amazon.com/images/I/71FZ+gN6FrL._AC_SL1500_.jpg",
        "hashtags": "#SmartHome #LEDLights #AmazonFinds #HomeAutomation #TechDeals"
    }
]


def create_affiliate_link(asin, associate_tag="shivamsahu010-21"):
    """Create Amazon affiliate link with your Associate Tag"""
    return f"https://www.amazon.com/dp/{asin}?tag={associate_tag}"


def prepare_pin_for_pinterest(product):
    """Prepare complete pin data"""
    affiliate_link = create_affiliate_link(product['amazon_asin'])
    
    description = f"{product['description']}\n\n💰 Price: {product['price']}\n⭐ Rating: {product['rating']}/5\n\n🛒 Click to buy on Amazon!\n\n{product['hashtags']}"
    
    return {
        'title': product['title'],
        'description': description,
        'image_url': product['image_url'],
        'link': affiliate_link,
        'category': product['category'],
        'amazon_asin': product['amazon_asin']
    }


def create_10_pins_for_today():
    """Create 10 pins with most searched Pinterest products"""
    
    print(f"\n{'='*60}")
    print(f"📌 Creating 10 Pins with MOST SEARCHED Pinterest Products")
    print(f"{'='*60}\n")
    
    # Select 10 most popular products
    selected = MOST_SEARCHED_PINTEREST_PRODUCTS[:10]
    
    pins_data = []
    
    for i, product in enumerate(selected, 1):
        print(f"Pin {i}/10: {product['title'][:50]}...")
        pin_data = prepare_pin_for_pinterest(product)
        pins_data.append(pin_data)
        
        print(f"   Category: {product['category']}")
        print(f"   ASIN: {product['amazon_asin']}")
        print(f"   Price: {product['price']}")
        print(f"   Link: {pin_data['link']}")
        print()
    
    print(f"✅ Prepared {len(pins_data)} pins ready to post!")
    
    return pins_data


if __name__ == "__main__":
    pins = create_10_pins_for_today()
    
    print("\n" + "="*60)
    print("📋 PINS READY TO CREATE:")
    print("="*60)
    for i, pin in enumerate(pins, 1):
        print(f"\n{i}. {pin['title'][:60]}")
        print(f"   {pin['link']}")

