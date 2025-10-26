#!/bin/bash
# One-Command GitHub Deployment

echo "🚀 Deploying to GitHub - Fully Automated Setup"
echo "=============================================="
echo ""

# Check if remote exists
if git remote get-url origin &> /dev/null; then
    echo "✅ GitHub remote already configured"
    REMOTE_URL=$(git remote get-url origin)
    echo "   Remote: $REMOTE_URL"
    echo ""
    echo "Pushing to GitHub..."
    git push -u origin main
    echo ""
    echo "✅ Successfully pushed to GitHub!"
else
    echo "📝 Need to set up GitHub remote first"
    echo ""
    echo "Please provide your GitHub username:"
    read GITHUB_USERNAME
    
    echo ""
    echo "Creating remote and pushing..."
    git remote add origin https://github.com/$GITHUB_USERNAME/pinterest-automation.git
    git branch -M main
    git push -u origin main
    
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
fi

echo ""
echo "📋 Next Steps:"
echo "   1. Go to: https://github.com/$GITHUB_USERNAME/pinterest-automation/settings/secrets/actions"
echo "   2. Click 'New repository secret'"
echo "   3. Add:"
echo "      Name: AMAZON_ASSOCIATE_TAG"
echo "      Value: shivamsahu010-21"
echo "   4. Go to Actions tab and enable workflows"
echo ""
echo "🎉 That's it! Your automation will run daily automatically!"

