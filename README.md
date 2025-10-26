# Pinterest-Amazon Affiliate Automation

Automated system to research trending products on Pinterest, find them on Amazon, and create Pinterest pins with your Amazon affiliate links.

## 🎯 Features

- **Trending Product Research**: Automatically finds most searched products on Pinterest
- **Amazon Product Search**: Searches for products on Amazon with fallback options
- **Image Optimization**: Upscales and optimizes product images for Pinterest
- **Smart Posting**: Random time posting to appear more natural
- **Duplicate Prevention**: Tracks posted products to avoid duplicates
- **Affiliate Link Tracking**: Adds UTM parameters for tracking

## 📋 Prerequisites

Before starting, you'll need:

### 1. Amazon Product Advertising API (PA-API) Credentials

Sign up for Amazon Associates and get PA-API credentials:
- Access Key
- Secret Key  
- Associate Tag (your affiliate ID)

Apply here: https://webservices.amazon.com/paapi5/documentation/

### 2. Pinterest API Access

Already configured via Activepieces MCP server ✅

### 3. Replicate API (Optional - for image upscaling)

Sign up at https://replicate.com/ and get API key

### 4. Python 3.8+

## 🚀 Installation

1. **Install dependencies:**
```bash
cd pinterest_amazon_automation
pip install -r requirements.txt
```

2. **Configure the system:**

Edit `config.json` with your credentials:

```json
{
  "amazon": {
    "access_key": "YOUR_AMAZON_ACCESS_KEY",
    "secret_key": "YOUR_AMAZON_SECRET_KEY",
    "associate_tag": "YOUR_AMAZON_ASSOCIATE_TAG"
  },
  "pinterest": {
    "account_token": "YOUR_PINTEREST_TOKEN"
  },
  "image_processing": {
    "replicate_api_key": "YOUR_REPLICATE_API_KEY"
  }
}
```

3. **Set up Pinterest boards:**

Create boards in your Pinterest account where pins will be posted:
- "Amazon Finds"
- "Trending Products"  
- "Best Deals"

Update board names in `config.json` if different.

## 📊 How It Works

### Daily Automation Flow:

1. **Research Phase** (Automatic)
   - Searches Pinterest for trending products by category
   - Identifies most searched keywords
   - Ranks products by popularity

2. **Product Search** (Automatic)
   - Searches Amazon for each trending product
   - Extracts product details (title, price, images, description)
   - Generates affiliate link
   - Falls back to alternative if not found

3. **Image Processing** (Automatic)
   - Downloads product images from Amazon
   - Upscales images if needed (via Replicate or simple resizing)
   - Optimizes for Pinterest (1000x1500px recommended)
   - Ensures proper aspect ratio

4. **Pin Creation** (Automatic)
   - Creates engaging pin description
   - Adds relevant hashtags
   - Includes affiliate link with tracking
   - Posts to selected Pinterest board at random time

5. **Tracking** (Automatic)
   - Saves posted products to database
   - Prevents duplicate posts (7-day cooldown)
   - Generates daily statistics

## ⚙️ Configuration

### Posting Schedule

Edit `config.json` to set posting times:

```json
"automation": {
  "post_times": [
    {"hour": 9, "minute": 30},   // 9:30 AM
    {"hour": 14, "minute": 15},  // 2:15 PM
    {"hour": 18, "minute": 45},  // 6:45 PM
    {"hour": 21, "minute": 20}   // 9:20 PM
  ],
  "random_time_range": 30,       // ±30 minutes random offset
  "pins_per_day": 3,            // Max pins per day
  "include_fallback": true       // Try alternative if not found
}
```

### Product Research Keywords

Customize trending product categories:

```json
"product_research": {
  "top_keywords": [
    "home decor",
    "kitchen gadgets",
    "fitness equipment",
    "tech accessories",
    "beauty products"
  ],
  "trending_categories": [
    "electronics",
    "home-improvement",
    "sports-outdoors",
    "beauty-personal-care"
  ]
}
```

## 🎮 Usage

### Run Once (Test)

```bash
python main_automation.py --now
```

This will run one complete cycle immediately:
- Research trending products
- Find on Amazon
- Create and post one pin

### Start Daily Automation

```bash
python main_automation.py
```

This starts the scheduler that will:
- Run automatically at configured times
- Post random times within ±30 minutes
- Respect daily posting limits
- Continue running in background

### Run with Cron (Recommended)

Add to your crontab for automatic daily execution:

```bash
# Edit crontab
crontab -e

# Add line (runs every day at 9 AM)
0 9 * * * cd /path/to/pinterest_amazon_automation && python main_automation.py --now
```

## 📈 Analytics & Tracking

### View Posted Products

```python
from database import get_stats

stats = get_stats()
print(stats)
```

Output:
```json
{
  "total": 45,
  "successful": 43,
  "failed": 2,
  "last_7_days": 21,
  "last_30_days": 45
}
```

### Check Database

View `posted_products.json` for complete history:
```bash
cat posted_products.json
```

## 🛠️ Customization

### Add Custom Keywords

Edit `config.json`:
```json
"product_research": {
  "top_keywords": [
    "your custom keyword",
    "another keyword"
  ]
}
```

### Change Image Upscaling Method

Options in config:
- `replicate`: Use Replicate API (best quality, costs money)
- `pil`: Use PIL/Pillow (free, basic upscaling)

### Modify Pin Description Format

Edit `pin_creator.py` in `create_pin_description()` method.

## 🔍 Troubleshooting

### "Amazon product not found"

Solution:
1. Enable fallback in config: `"include_fallback": true`
2. Add more specific keywords
3. System will try alternative search terms

### "Image processing failed"

Solution:
1. Check internet connection
2. Verify Replicate API key (if using)
3. Ensure Amazon images are accessible
4. Check image_processor.py logs

### "Failed to create Pinterest pin"

Solution:
1. Verify Pinterest MCP connection
2. Check board names in config match your Pinterest boards
3. Ensure valid affiliate links
4. Check pin_creator.py error logs

### "Daily limit reached"

This is normal! System respects daily limits to:
- Appear natural
- Avoid spam
- Follow Pinterest guidelines

## 💡 Tips for Best Results

1. **Focus on Quality Keywords**: Use keywords people actually search for
2. **Check Trending Products**: Update keywords monthly based on trends
3. **Monitor Performance**: Track which products get clicks
4. **Vary Posting Times**: System randomizes times automatically
5. **Use High-Quality Images**: Enable Replicate upscaling for better results
6. **Review Posted Products**: Check `posted_products.json` regularly

## 🔐 Security Notes

- Never commit `config.json` with real credentials
- Add `config.json` to `.gitignore`
- Rotate API keys regularly
- Monitor API usage to avoid limits

## 📝 Important: Amazon Associates Compliance

⚠️ Always comply with Amazon Associates Operating Agreement:

- Disclose affiliate relationships in pin descriptions
- Don't create misleading pins
- Follow FTC guidelines for affiliate disclosures
- Don't engage in deceptive practices

Example disclosure in pin:
> "🛒 Click link to buy on Amazon! [Affiliate Disclosure]"

## 🚀 Next Steps

After setup:

1. Run test: `python main_automation.py --now`
2. Verify first pin was created
3. Check Amazon affiliate link works
4. Start daily automation
5. Monitor performance in Amazon Associates dashboard

## 📞 Support

For issues or questions:
- Check troubleshooting section above
- Review logs in `automation.log`
- Verify API credentials are valid
- Ensure all dependencies installed

## 📄 License

This automation tool is for personal use. Ensure compliance with:
- Amazon Associates Operating Agreement
- Pinterest Terms of Service
- FTC Disclosure Guidelines

