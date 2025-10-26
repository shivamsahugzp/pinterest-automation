# 🤖 Fully Automated Pinterest Pin System

## 🎯 What This Does
Automatically posts **10 Pinterest pins** every day at random times throughout the day - completely hands-free!

---

## 📋 Setup Options

### Option 1: Local Cron Job (Best for Personal Use) ⭐ RECOMMENDED

**Advantages:**
- ✅ No cost
- ✅ Runs even when laptop is closed (if Mac stays on)
- ✅ Instant setup
- ✅ No GitHub needed

**Setup:**
```bash
cd pinterest_amazon_automation
chmod +x setup_cron.sh
./setup_cron.sh
```

**How it works:**
- Runs daily at 8:00 AM (configurable)
- Posts 10 pins throughout the day automatically
- Logs saved to `logs/daily_pins.log`

---

### Option 2: GitHub Actions (Best for Always-On) ⭐ RECOMMENDED

**Advantages:**
- ✅ Runs even when laptop is OFF
- ✅ Free for public repos
- ✅ Automatic from anywhere
- ✅ Version control

**Setup:**

1. **Push to GitHub:**
```bash
cd pinterest_amazon_automation
git init
git add .
git commit -m "Add automated Pinterest system"
git remote add origin https://github.com/YOUR_USERNAME/pinterest-automation.git
git push -u origin main
```

2. **Add Secrets to GitHub:**
   - Go to: https://github.com/YOUR_USERNAME/pinterest-automation/settings/secrets
   - Add these secrets:
     - `AMAZON_ASSOCIATE_TAG`: `shivamsahu010-21`
     - `PINTEREST_TOKEN`: Your Pinterest token
     - `REPLICATE_API_KEY`: (optional) Your Replicate API key

3. **That's it!**
   - GitHub will automatically run daily at 8:00 AM UTC
   - You can manually trigger from GitHub Actions tab

---

## ⚙️ Configuration

Edit `config.json`:
```json
{
  "associate_tag": "shivamsahu010-21",
  "board_name": "MCP Test Board",
  "posts_per_day": 10
}
```

---

## 📊 Daily Schedule

Pins are posted at these times (automatically):
- 8:30 AM - Morning
- 9:15 AM - Morning  
- 11:00 AM - Late morning
- 12:45 PM - Lunch time
- 2:30 PM - Afternoon
- 3:45 PM - Afternoon
- 5:15 PM - Evening
- 6:45 PM - Evening
- 8:30 PM - Night
- 9:15 PM - Night

**10 pins total per day** - spread throughout the day naturally!

---

## 🎯 What Gets Posted

Each day, the system randomly selects 10 products from 30+ most searched Pinterest products:

**Categories:**
- Home Decor (most searched!)
- Kitchen Appliances
- Fitness Equipment
- Beauty Products
- Tech Accessories
- Office Supplies
- Smart Home Devices
- Organization Items

**Each pin includes:**
- ✅ Real Amazon product images
- ✅ Complete product descriptions
- ✅ Prices and ratings
- ✅ Your affiliate link (tag=shivamsahu010-21)
- ✅ Relevant hashtags

---

## 💰 Earnings Potential

**If 1 person buys from each daily pin:**
- Daily sales: ~$647
- Daily commission: $13-$26
- Monthly potential: $390-$780

**Even if only 10% buy (1 sale per day):**
- Monthly commission: $39-$78

---

## 🔍 Monitoring

### View Logs (Cron Method):
```bash
tail -f logs/daily_pins.log
```

### Check Cron Status:
```bash
crontab -l
```

### View GitHub Action Results:
- Go to: https://github.com/YOUR_USERNAME/pinterest-automation/actions

---

## 🛠️ Troubleshooting

### Cron Not Running?
```bash
# Check if cron is installed
sudo launchctl list | grep cron

# Restart cron (Mac)
sudo launchctl stop com.apple.cron
sudo launchctl start com.apple.cron
```

### GitHub Actions Not Running?
- Check workflow tab for errors
- Verify secrets are added correctly
- Check workflow file exists: `.github/workflows/daily_pins.yml`

### Want Different Posting Times?
Edit `daily_automated_pins.py` → `get_daily_posting_schedule()` function

---

## 🚀 Quick Start Commands

### Setup (One-time):
```bash
cd pinterest_amazon_automation
./setup_cron.sh
```

### Run Once (Test):
```bash
python daily_automated_pins.py
```

### View Status:
```bash
crontab -l
tail logs/daily_pins.log
```

### Remove Automation:
```bash
crontab -l | grep -v daily_automated_pins.py | crontab -
```

---

## ✅ Done!

Your system will now:
- ✅ Post 10 pins daily automatically
- ✅ Post at random times throughout the day
- ✅ Use your affiliate links
- ✅ Track everything in logs
- ✅ Work even when laptop is closed (GitHub method)

**No more manual work needed!** 🎉

