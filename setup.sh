#!/bin/bash

echo "🚀 Setting up Pinterest-Amazon Automation"
echo "=========================================="
echo ""

# Check Python version
echo "📋 Checking Python installation..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
if [ $? -eq 0 ]; then
    echo "✅ Python $python_version found"
else
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create directories
echo ""
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p images

# Check config file
echo ""
if [ -f "config.json" ]; then
    echo "✅ config.json found"
    echo ""
    echo "⚠️  IMPORTANT: Please edit config.json with your credentials:"
    echo "   - Amazon Access Key"
    echo "   - Amazon Secret Key"
    echo "   - Amazon Associate Tag"
    echo "   - Pinterest Token"
    echo "   - Replicate API Key (optional)"
else
    echo "❌ config.json not found"
    echo "Creating from template..."
    # config.json already created earlier
fi

# Create .gitignore
echo ""
echo "🔒 Creating .gitignore..."
cat > .gitignore << EOF
config.json
*.pyc
__pycache__/
venv/
.env
*.log
posted_products.json
images/
temp_*
*_upscaled.jpg
*_pinterest_optimized.jpg
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Edit config.json with your API credentials"
echo "   2. Run test: python main_automation.py --now"
echo "   3. Start automation: python main_automation.py"
echo ""
echo "📚 For more information, see README.md"
echo ""

