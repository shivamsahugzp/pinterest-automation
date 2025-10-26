#!/bin/bash
# Setup Cron Job for Automated Pinterest Pins

echo "🚀 Setting up Automated Pinterest Pin Posting"
echo "=============================================="
echo ""

# Get the absolute path of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/daily_automated_pins.py"

echo "📁 Script directory: $SCRIPT_DIR"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found"

# Create log directory
mkdir -p logs
echo "✅ Log directory created"

# Add cron job
CRON_JOB="0 8 * * * cd $SCRIPT_DIR && /usr/bin/python3 daily_automated_pins.py >> logs/daily_pins.log 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "daily_automated_pins.py"; then
    echo "⚠️  Cron job already exists. Updating..."
    crontab -l 2>/dev/null | grep -v "daily_automated_pins.py" | crontab -
fi

# Add new cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo ""
echo "✅ Cron job added successfully!"
echo ""
echo "📋 Current cron jobs:"
crontab -l

echo ""
echo "📝 Your cron job will run daily at 8:00 AM"
echo "📊 Logs will be saved to: logs/daily_pins.log"
echo ""
echo "To view logs:"
echo "  tail -f logs/daily_pins.log"
echo ""
echo "To remove cron job:"
echo "  crontab -l | grep -v daily_automated_pins.py | crontab -"
echo ""

