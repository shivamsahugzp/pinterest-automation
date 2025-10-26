#!/bin/bash
# Quick GitHub Deployment Script

echo "🚀 Deploying Pinterest Automation to GitHub"
echo "==========================================="
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
fi

# Check for changes
if git diff --quiet && git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    echo "📝 Committing changes..."
    git add .
    git commit -m "Update: Automated Pinterest pin system"
fi

# Get GitHub username
echo "📝 Enter your GitHub username:"
read GITHUB_USERNAME

# Set up remote if not exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/$GITHUB_USERNAME/pinterest-automation.git
fi

# Ask to create repository
echo ""
echo "📋 Have you created the GitHub repository yet?"
echo "   1) Yes, repository already exists"
echo "   2) No, I need to create it"
read -p "Enter choice (1 or 2): " choice

if [ "$choice" == "2" ]; then
    echo ""
    echo "Please create the repository at: https://github.com/new"
    echo "Repository name: pinterest-automation"
    echo "Make it PUBLIC (required for free GitHub Actions)"
    echo ""
    read -p "Press ENTER when repository is created..."
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Successfully deployed to GitHub!"
echo ""
echo "📋 Next steps:"
echo "   1. Go to: https://github.com/$GITHUB_USERNAME/pinterest-automation/settings/secrets/actions"
echo "   2. Add secret: AMAZON_ASSOCIATE_TAG = shivamsahu010-21"
echo "   3. Your automation will run daily at 8:00 AM UTC"
echo ""
echo "🎉 Done! Your pins will post automatically every day!"

