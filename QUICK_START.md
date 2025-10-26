# 🚀 Quick Start Guide

Get your Pinterest-Amazon automation running in 15 minutes!

## Step 1: Setup (5 minutes)

```bash
# Navigate to project
cd pinterest_amazon_automation

# Run setup script
./setup.sh

# Edit config with your credentials
nano config.json
```

Add your credentials to `config.json`:

```json
{
  "amazon": {
    "access_key": "AKIA...",
    "secret_key": "wJalrXUt...",
    "associate_tag": "yourname-20"
  }
}
```

## Step 2: Get Amazon API Credentials (5 minutes)

1. Go to: https://webservices.amazon.com/paapi5/documentation/
2. Sign up for Amazon Associates
3. Apply for Product Advertising API
4. Get your:
   - Access Key ID
   - Secret Access Key  
   - Associate Tag

## Step 3: Test It! (5 minutes)

```bash
# Run a test post
python main_automation.py --now
```

This will:
- ✅ Research trending Pinterest products
- ✅ Find product on Amazon
- ✅ Create pin description
- ✅ Show you the pin that would be posted

## Step 4: Start Daily Automation

```bash
# Start scheduler (runs in background)
python main_automation.py
```

Now it will automatically:
- 📅 Post at scheduled times (with random ±30min)
- 🎯 Post 3 pins per day max
- 🔄 Avoid duplicate posts
- 📊 Track all activity

## 📊 What Gets Posted?

Each pin includes:
- 📸 Optimized product image
- ✨ Engaging title with emojis
- 💰 Product price and rating
- 🔗 Your Amazon affiliate link with tracking
- 🏷️ Relevant hashtags
- 📝 Compelling description

## ⚙️ Customize Posting Times

Edit `config.json`:

```json
"automation": {
  "post_times": [
    {"hour": 9, "minute": 0},   // 9 AM
    {"hour": 14, "minute": 0},  // 2 PM  
    {"hour": 19, "minute": 0}   // 7 PM
  ],
  "random_time_range": 30,      // Random ±30 min
  "pins_per_day": 3
}
```

## 🎯 Customize Products

Change what products to feature:

```json
"product_research": {
  "top_keywords": [
    "smart home devices",
    "fitness gear",
    "beauty products"
  ]
}
```

## 📈 Monitor Performance

```bash
# View posted products
cat posted_products.json

# Check stats
python -c "from database import get_stats; print(get_stats())"
```

## 🛠️ Troubleshooting

### No pins being created?

1. Check Amazon API credentials
2. Verify Pinterest connection (MCP should be working)
3. Check `automation.log` for errors

### Image processing fails?

1. Install Replicate for better quality, OR
2. Use free PIL upscaling (change in config)
3. Check image URLs are accessible

### No products found?

1. Expand keywords in `config.json`
2. Enable fallback: `"include_fallback": true`
3. System will try alternative searches

## 🎉 You're Done!

Your automation will now:
- ✅ Post 3 pins/day at random times
- ✅ Feature trending Pinterest products
- ✅ Include your Amazon affiliate links
- ✅ Track all activity
- ✅ Avoid duplicates

## 💰 Next: Make Money

1. Share your Pinterest boards
2. Track clicks in Amazon Associates
3. Monitor which products convert
4. Adjust keywords based on performance

Happy automating! 🚀

