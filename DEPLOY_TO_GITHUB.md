# 🚀 Deploy to GitHub - Step by Step Guide

## Quick Setup (5 minutes)

### Step 1: Initialize Git Repository
```bash
cd pinterest_amazon_automation
git init
git add .
git commit -m "Initial commit: Automated Pinterest pin system"
```

### Step 2: Create GitHub Repository
1. Go to: https://github.com/new
2. Repository name: `pinterest-automation`
3. Description: "Automated Pinterest pin posting with Amazon affiliate links"
4. Make it **Public** (free GitHub Actions)
5. Click "Create repository"

### Step 3: Connect and Push
```bash
git remote add origin https://github.com/YOUR_USERNAME/pinterest-automation.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 4: Add Secrets (Amazon Associate Tag)
1. Go to: https://github.com/YOUR_USERNAME/pinterest-automation/settings/secrets/actions
2. Click "New repository secret"
3. Add these secrets:
   - Name: `AMAZON_ASSOCIATE_TAG`
   - Value: `shivamsahu010-21`
4. Add another:
   - Name: `PINTEREST_TOKEN`
   - Value: (if needed)
5. Save

### Step 5: Enable GitHub Actions
1. Go to: https://github.com/YOUR_USERNAME/pinterest-automation/actions
2. Click "I understand my workflows" if prompted
3. Your workflow will run daily at 8:00 AM UTC

---

## ✅ That's It!

Your automation is now live on GitHub and will:
- ✅ Run daily at 8:00 AM UTC
- ✅ Post 10 pins throughout the day
- ✅ Use your affiliate links automatically
- ✅ Work even when your laptop is closed

---

## 🎯 Manual Run
To trigger manually:
1. Go to: https://github.com/YOUR_USERNAME/pinterest-automation/actions
2. Click "Daily Pinterest Pins Automation"
3. Click "Run workflow"
4. Click green "Run workflow" button

---

## 📊 Monitor Results
- View logs in Actions tab
- Check commit history for auto-commits
- View posted products in database

---

## 🔗 Your Repository
Once deployed, your repo will be at:
`https://github.com/YOUR_USERNAME/pinterest-automation`

