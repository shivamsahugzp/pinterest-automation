# 🔧 Implementation Guide - MCP Integration

This guide explains how to integrate the actual MCP Pinterest tools into the automation.

## Available MCP Tools

Your Pinterest MCP server provides these tools:

### 1. Create Pin (`mcp_Activepieces_createPin_O7u7`)
```python
# Usage
result = mcp_Activepieces_createPin_O7u7(
    instructions={
        "board_id": "board_id_here",
        "image_url": "https://example.com/image.jpg",
        "title": "Product Title",
        "description": "Product description here",
        "link": "https://amazon.com/dp/B123/?tag=yours-20"
    }
)
```

### 2. Find Board (`mcp_Activepieces_findBoardByName_vCjY`)
```python
result = mcp_Activepieces_findBoardByName_vCjY(
    instructions="Find board named 'Amazon Finds'"
)
```

### 3. Other Available Tools
- `mcp_Activepieces_deletePin_5gpH` - Delete a pin
- `mcp_Activepieces_findPin_mBV0` - Find pins by keyword
- `mcp_Activepieces_createBoard_S1eC` - Create new board
- `mcp_Activepieces_updateBoard_gdum` - Update board details

## Complete Implementation Example

Here's how to update the automation to use real MCP tools:

### Update main_automation.py

```python
def _create_pinterest_pin(self, product: Dict, image_path: str) -> bool:
    """Create Pinterest pin via MCP"""
    try:
        # Step 1: Get board
        board_name = self.config.get('board_settings', {}).get('boards', ['Amazon Finds'])[0]
        
        board_result = mcp_Activepieces_findBoardByName_vCjY(
            instructions=f"Find board named '{board_name}'"
        )
        
        if not board_result.get('items'):
            # Create board if doesn't exist
            print(f"Creating board: {board_name}")
            create_result = mcp_Activepieces_createBoard_S1eC(
                instructions={
                    "name": board_name,
                    "description": "Curated Amazon product finds"
                }
            )
            board_id = create_result.get('id')
        else:
            board_id = board_result['items'][0]['id']
        
        # Step 2: Prepare pin data
        pin_data = prepare_pin_for_creation(product, image_path, self.config)
        
        # Step 3: Upload image first
        # Note: You may need to upload image to a hosting service
        # Pinterest's API requires the image to be accessible via URL
        image_url = self._upload_image_to_hosting(image_path)
        
        # Step 4: Create pin
        pin_result = mcp_Activepieces_createPin_O7u7(
            instructions={
                "board_id": board_id,
                "image_url": image_url,
                "title": pin_data['title'],
                "description": pin_data['description'],
                "link": product.get('affiliate_link', '')
            }
        )
        
        if pin_result:
            print(f"✅ Pin created: {pin_result.get('url', 'N/A')}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False
```

## Image Upload Strategy

Pinterest requires images to be accessible via URL. Options:

### Option 1: Imgur API (Free)
```python
import requests

def _upload_image_to_hosting(self, image_path: str) -> str:
    """Upload image to Imgur and get URL"""
    import requests
    
    headers = {'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'}
    with open(image_path, 'rb') as img:
        response = requests.post(
            'https://api.imgur.com/3/image',
            headers=headers,
            files={'image': img}
        )
    
    return response.json()['data']['link']
```

### Option 2: Pinterest Upload (Recommended)
```python
def _upload_to_pinterest(self, image_path: str) -> str:
    """Upload image directly to Pinterest"""
    # Use Pinterest media upload endpoint
    # Returns media_id or URL
    pass
```

## Amazon Affiliate Link Setup

### Get Your Associate Tag

1. Sign up at: https://affiliate-program.amazon.com/
2. Get your Associate Tag (e.g., `yourname-20`)
3. Add to `config.json`:

```json
{
  "amazon": {
    "access_key": "...",
    "secret_key": "...",
    "associate_tag": "yourname-20"
  }
}
```

### UTM Tracking

The automation automatically adds UTM parameters:

```
Original: https://amazon.com/dp/B123/?tag=yourname-20
With UTM: https://amazon.com/dp/B123/?tag=yourname-20&utm_source=pinterest&utm_medium=pin
```

## Complete Flow Diagram

```
1. Research Trending Products (Pinterest)
   ↓
2. Search Amazon (PA-API)
   ↓
3. Extract Product Details
   ↓
4. Process Image (Upscale & Optimize)
   ↓
5. Generate Affiliate Link
   ↓
6. Create Pin (Pinterest via MCP)
   ↓
7. Track in Database
   ↓
8. Schedule Next Post
```

## Testing MCP Integration

Test your MCP connection:

```python
# test_mcp.py
from main_automation import PinterestAmazonAutomation

automation = PinterestAmazonAutomation()
success = automation.research_and_post_cycle()

if success:
    print("✅ Test passed!")
else:
    print("❌ Test failed - check logs")
```

## Debugging Tips

### Check MCP Connection
```python
# In your MCP environment
from tools import mcp_Activepieces_findBoardByName_vCjY

result = mcp_Activepieces_findBoardByName_vCjY(
    instructions="Find board named 'Test Board'"
)
print(result)
```

### View Logs
```bash
tail -f automation.log
```

### Test Individual Components
```python
# Test Pinterest research
python pinterest_research.py

# Test Amazon search
python amazon_search.py

# Test image processing
python image_processor.py
```

## Security Best Practices

1. **Never commit credentials**:
   ```bash
   echo "config.json" >> .gitignore
   echo "posted_products.json" >> .gitignore
   ```

2. **Use environment variables**:
   ```python
   import os
   amazon_key = os.environ.get('AMAZON_ACCESS_KEY')
   ```

3. **Rotate API keys**:
   - Monthly rotation recommended
   - Update in config.json immediately

## Production Deployment

### Run as Service (Linux)
```bash
# Create systemd service
sudo nano /etc/systemd/system/pinterest-automation.service

[Unit]
Description=Pinterest-Amazon Automation
After=network.target

[Service]
Type=simple
User=yourname
WorkingDirectory=/path/to/pinterest_amazon_automation
ExecStart=/usr/bin/python3 main_automation.py
Restart=always

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable pinterest-automation
sudo systemctl start pinterest-automation
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main_automation.py"]
```

## Next Steps

1. ✅ Set up Amazon PA-API credentials
2. ✅ Configure Pinterest board names
3. ✅ Test MCP connection
4. ✅ Run test post: `python main_automation.py --now`
5. ✅ Start automation: `python main_automation.py`
6. ✅ Monitor performance in Amazon Associates dashboard

Good luck! 🚀

