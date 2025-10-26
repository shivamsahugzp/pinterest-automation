# Pinterest-Amazon Affiliate Automation - Project Summary

## 🎯 What Was Created

A complete automated system that:
1. **Researches trending products** on Pinterest daily
2. **Finds matching products** on Amazon
3. **Creates optimized pins** with your Amazon affiliate links
4. **Posts at random times** to appear natural
5. **Tracks everything** to avoid duplicates

## 📁 Project Structure

```
pinterest_amazon_automation/
├── main_automation.py          # Main orchestrator - coordinates everything
├── pinterest_research.py        # Research trending Pinterest products
├── amazon_search.py            # Search Amazon products & generate affiliate links
├── image_processor.py           # Optimize images for Pinterest
├── pin_creator.py               # Create engaging pin descriptions
├── mcp_integration.py           # Connect to Pinterest via MCP
├── scheduler.py                 # Random time scheduling
├── database.py                  # Track posted products
├── config.json                  # Configuration (credentials, settings)
├── requirements.txt            # Python dependencies
├── setup.sh                     # Quick setup script
├── README.md                    # Complete documentation
├── QUICK_START.md               # 15-minute setup guide
├── IMPLEMENTATION_GUIDE.md      # MCP integration details
└── PROJECT_SUMMARY.md           # This file

Generated files (at runtime):
├── posted_products.json         # Database of posted products
├── automation.log               # Execution logs
└── images/                      # Downloaded/processed images
```

## 🔄 How It Works

### Daily Automation Flow

```
START
  │
  ├─→ Research Pinterest Trends
  │     • Find trending keywords
  │     • Rank by popularity
  │     • Select best product
  │
  ├─→ Search Amazon
  │     • Find product on Amazon
  │     • Extract details (title, price, images)
  │     • Generate affiliate link
  │     • Fallback if not found
  │
  ├─→ Process Images
  │     • Download from Amazon
  │     • Upscale if needed
  │     • Optimize for Pinterest (1000x1500px)
  │
  ├─→ Create Pin
  │     • Generate engaging description
  │     • Add hashtags
  │     • Include affiliate link
  │     • Post to Pinterest via MCP
  │
  ├─→ Track & Save
  │     • Save to database
  │     • Avoid duplicates (7-day cooldown)
  │
  └─→ Schedule Next
        • Random time (within ±30 min)
        • Daily limit (3 pins/day)

END
```

## ⚙️ Key Features

### 1. Pinterest Product Research (`pinterest_research.py`)
- Searches trending keywords
- Ranks by popularity score
- Returns top products to feature

### 2. Amazon Product Search (`amazon_search.py`)
- Searches via Product Advertising API
- Extracts product details
- Generates affiliate links with UTM tracking
- Fallback to alternatives if not found

### 3. Image Processing (`image_processor.py`)
- Downloads product images
- Upscales using Replicate or PIL
- Optimizes for Pinterest (2:3 aspect ratio)
- Saves to disk

### 4. Pin Creation (`pin_creator.py`)
- Creates engaging descriptions
- Adds price, rating, hashtags
- Formats affiliate links
- Includes call-to-action

### 5. MCP Integration (`mcp_integration.py`)
- Connects to Pinterest via Activepieces MCP
- Finds/creates boards
- Posts pins with images

### 6. Smart Scheduling (`scheduler.py`)
- Posts at configurable times
- Random ±30 minute offset
- Respects daily limits

### 7. Database Tracking (`database.py`)
- Tracks all posted products
- Prevents 7-day duplicates
- Generates statistics

## 🎨 Example Output

### Pin Description Format:
```
🔥 Premium Smart Home Camera - Amazon Best Seller!

WiFi security camera with night vision and motion detection.
Perfect for home security and peace of mind.

💰 Price: $49.99
⭐ Rating: 4.5/5

🛒 Click link to buy on Amazon!

#HomeSecurity #SmartHome #AmazonFinds #BestProducts #MustHave
```

## 📊 Configuration Options

### Posting Times
```json
"post_times": [
  {"hour": 9, "minute": 30},
  {"hour": 14, "minute": 15},
  {"hour": 18, "minute": 45}
]
```

### Keywords
```json
"top_keywords": [
  "home decor",
  "kitchen gadgets",
  "fitness equipment"
]
```

### Daily Limits
```json
"pins_per_day": 3,
"random_time_range": 30
```

## 🚀 Getting Started

1. **Setup** (5 min):
   ```bash
   cd pinterest_amazon_automation
   ./setup.sh
   nano config.json  # Add credentials
   ```

2. **Test** (5 min):
   ```bash
   python main_automation.py --now
   ```

3. **Start**:
   ```bash
   python main_automation.py
   ```

## 📈 Expected Results

With default settings:
- **3 pins per day** at random times
- **Trending products** from Pinterest
- **Amazon affiliate links** with UTM tracking
- **Optimized images** for Pinterest
- **No duplicates** (7-day cooldown)
- **Natural posting** (randomized times)

## 🔧 Required Setup

### 1. Amazon Product Advertising API
- Sign up: https://webservices.amazon.com/paapi5/
- Get: Access Key, Secret Key, Associate Tag
- Add to `config.json`

### 2. Pinterest MCP Connection
- ✅ Already configured in Cursor MCP
- Activepieces endpoint working
- Can create pins, boards, etc.

### 3. Replicate API (Optional)
- Sign up: https://replicate.com/
- Get API key for image upscaling
- OR use free PIL method

## 💡 Customization Ideas

### Add More Keywords
Edit `config.json` → `product_research.top_keywords`

### Change Posting Schedule
Edit `config.json` → `automation.post_times`

### Modify Pin Descriptions
Edit `pin_creator.py` → `create_pin_description()`

### Add Image Filters
Edit `image_processor.py` → `optimize_for_pinterest()`

## 🎓 What You Need to Provide

1. **Amazon API Credentials**:
   - Access Key
   - Secret Key
   - Associate Tag (your affiliate ID)

2. **Pinterest Board Names**:
   - Already working via MCP!
   - Create boards in Pinterest
   - List names in `config.json`

3. **Optional: Replicate API Key**:
   - For better image upscaling
   - Free alternative: PIL method

## 📝 Next Steps

1. ✅ Run setup: `./setup.sh`
2. ✅ Add credentials to `config.json`
3. ✅ Test: `python main_automation.py --now`
4. ✅ Start: `python main_automation.py`
5. ✅ Monitor in Amazon Associates dashboard

## 🎉 Success!

Your Pinterest-Amazon automation is ready to generate affiliate income through automated pin creation!

---

**Questions?** Check `README.md` or `QUICK_START.md` for detailed instructions.

