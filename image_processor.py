"""
Image Processing and Upscaling Module
Handles image downloads, upscaling, and Pinterest optimization
"""

import requests
from PIL import Image
import io
import os
from typing import List, Optional
import replicate


class ImageProcessor:
    def __init__(self, config: dict):
        self.config = config
        self.target_width = config.get('image_processing', {}).get('target_width', 1000)
        self.target_height = config.get('image_processing', {}).get('target_height', 1500)
        self.upscale_method = config.get('image_processing', {}).get('upscale_using', 'replicate')
        
        if self.upscale_method == 'replicate':
            self.replicate_api_key = config.get('image_processing', {}).get('replicate_api_key')
            if self.replicate_api_key:
                os.environ['REPLICATE_API_TOKEN'] = self.replicate_api_key
    
    def download_image(self, url: str, save_path: str = None) -> Optional[str]:
        """Download image from URL"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            image_data = response.content
            
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(image_data)
                return save_path
            else:
                # Return in-memory image
                return image_data
                
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
    
    def upscale_image(self, image_path: str, scale_factor: int = 2) -> Optional[str]:
        """
        Upscale image using chosen method
        Returns path to upscaled image
        """
        if self.upscale_method == 'replicate':
            return self._upscale_with_replicate(image_path)
        elif self.upscale_method == 'pil':
            return self._upscale_with_pil(image_path, scale_factor)
        else:
            # No upscaling
            return image_path
    
    def _upscale_with_replicate(self, image_path: str) -> Optional[str]:
        """Upscale image using Replicate API"""
        try:
            # Using ESRGAN model on Replicate
            output = replicate.run(
                "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
                input={"image": open(image_path, "rb")}
            )
            
            # Save upscaled image
            output_path = image_path.replace('.jpg', '_upscaled.jpg')
            
            if isinstance(output, str):
                response = requests.get(output)
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                
                return output_path
            
            return image_path
            
        except Exception as e:
            print(f"Error upscaling with Replicate: {e}")
            return image_path
    
    def _upscale_with_pil(self, image_path: str, scale_factor: int) -> Optional[str]:
        """Upscale image using PIL (simple method)"""
        try:
            img = Image.open(image_path)
            width, height = img.size
            
            new_size = (width * scale_factor, height * scale_factor)
            upscaled = img.resize(new_size, Image.LANCZOS)
            
            output_path = image_path.replace('.jpg', '_upscaled.jpg')
            upscaled.save(output_path, quality=95)
            
            return output_path
            
        except Exception as e:
            print(f"Error upscaling with PIL: {e}")
            return image_path
    
    def optimize_for_pinterest(self, image_path: str) -> Optional[str]:
        """
        Optimize image for Pinterest (2:3 aspect ratio recommended)
        Target: 1000x1500px
        """
        try:
            img = Image.open(image_path)
            width, height = img.size
            
            # Pinterest recommended aspect ratio: 2:3 (1000x1500)
            target_w, target_h = self.target_width, self.target_height
            
            # Resize maintaining aspect ratio
            if width != target_w or height != target_h:
                # Calculate resize that fits within target while maintaining ratio
                ratio = min(target_w / width, target_h / height)
                new_w = int(width * ratio)
                new_h = int(height * ratio)
                
                # Resize
                img_resized = img.resize((new_w, new_h), Image.LANCZOS)
                
                # Create canvas with target dimensions and paste centered
                canvas = Image.new('RGB', (target_w, target_h), (255, 255, 255))
                x = (target_w - new_w) // 2
                y = (target_h - new_h) // 2
                canvas.paste(img_resized, (x, y))
                
                # Save optimized image
                output_path = image_path.replace('.jpg', '_pinterest_optimized.jpg')
                canvas.save(output_path, quality=95, optimize=True)
                
                return output_path
            
            return image_path
            
        except Exception as e:
            print(f"Error optimizing for Pinterest: {e}")
            return image_path
    
    def process_product_images(self, image_urls: List[str], product_title: str) -> Optional[str]:
        """
        Download, upscale if needed, and optimize product images for Pinterest
        Returns path to final optimized image
        """
        if not image_urls:
            return None
        
        try:
            # Download first image
            temp_path = f"temp_{product_title.replace(' ', '_')}_image.jpg"
            downloaded = self.download_image(image_urls[0], temp_path)
            
            if not downloaded:
                return None
            
            # Upscale if needed
            upscaled_path = self.upscale_image(downloaded)
            if not upscaled_path:
                upscaled_path = downloaded
            
            # Optimize for Pinterest
            final_image = self.optimize_for_pinterest(upscaled_path)
            
            return final_image if final_image else upscaled_path
            
        except Exception as e:
            print(f"Error processing product images: {e}")
            return None
    
    def cleanup_temp_files(self, *file_paths):
        """Clean up temporary files"""
        for path in file_paths:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except Exception as e:
                print(f"Error cleaning up file {path}: {e}")


def optimize_image_for_pin(image_url: str, product_title: str, config: dict) -> Optional[str]:
    """
    Main function to optimize an image for Pinterest pin
    """
    processor = ImageProcessor(config)
    final_image = processor.process_product_images([image_url], product_title)
    return final_image


if __name__ == "__main__":
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Test image processing
    test_url = 'https://via.placeholder.com/500'
    optimized = optimize_image_for_pin(test_url, 'Test Product', config)
    print(f"Optimized image: {optimized}")

