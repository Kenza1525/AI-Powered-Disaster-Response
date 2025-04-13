import torch
from PIL import Image
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration
import os

class DisasterImageAnalyzer:
    def __init__(self):
        """Initialize the disaster image analyzer with BLIP model."""
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def load_image(self, image_path):
        """Load and preprocess an image."""
        if os.path.exists(image_path):
            image = Image.open(image_path).convert('RGB')
            return image
        else:
            raise FileNotFoundError(f"Image not found at {image_path}")

    def analyze_image(self, image_path):
        """Analyze a disaster image and generate a description."""
        try:
            # Load and preprocess the image
            image = self.load_image(image_path)
            
            # Prepare the image for the model
            inputs = self.processor(image, return_tensors="pt").to(self.device)
            
            # Generate description
            out = self.model.generate(**inputs, max_length=50)
            description = self.processor.decode(out[0], skip_special_tokens=True)
            
            return {
                "status": "success",
                "description": description,
                "image_path": image_path
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "image_path": image_path
            }

def main():
    # Example usage
    analyzer = DisasterImageAnalyzer()
    
    # Example image path - replace with your image path
    image_path = "path/to/your/disaster/image.jpg"
    
    result = analyzer.analyze_image(image_path)
    print(result)

if __name__ == "__main__":
    main() 