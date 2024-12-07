import cv2
import torch
import numpy as np
from PIL import Image
from lama_cleaner.model.base import DiffusionInpaintModel
from lama_cleaner.schema import Config
from lama_cleaner.model.lama import LaMa

class ImageCleanUp:
    def __init__(self):
        """
        Initialize the ImageCleanUp class
        Use lama-cleaner for image restoration
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = LaMa(device=self.device)

    def process_image(self, image_data):
        """
        Process the image and remove pink areas
        
        Parameters:
            image_data: binary image data
            
        Returns:
            inpainted_result: restored image
        
        Example usage:
            from image_clean_up import ImageCleanUp
            
            # Initialize the class
            cleaner = ImageCleanUp()
            
            # Read the image
            with open('image.jpg', 'rb') as f:
                image_data = f.read()
                
            # Process the image
            result = cleaner.process_image(image_data)
            
            # Save the result
            cv2.imwrite('result.jpg', result)
        """
        # Convert image data to OpenCV format
        nparr = np.frombuffer(image_data, np.uint8)
        self.img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Generate mask
        mask = self.create_mask_from_pink()
        
        # Use lama-cleaner for restoration
        config = Config(
            ldm_steps=20,
            ldm_sampler='plms',
            hd_strategy='Original',
            hd_strategy_crop_margin=32,
            hd_strategy_crop_trigger_size=200,
            hd_strategy_resize_limit=200,
        )
        
        return self.model(self.img, mask, config)

    def create_mask_from_pink(self):
        """
        Identify pink areas in the image and create a mask
        
        Returns:
            final_mask: mask of pink areas
        """
        # Convert to HSV color space
        hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        
        # Define the range for bright pink
        lower_pink = np.array([140, 100, 100])
        upper_pink = np.array([180, 255, 255])
        
        # Create initial mask
        initial_mask = cv2.inRange(hsv_img, lower_pink, upper_pink)
        
        # Use morphological operations to expand the mask area
        kernel = np.ones((5,5), np.uint8)
        dilated_mask = cv2.dilate(initial_mask, kernel, iterations=2)
        
        # Find connected regions
        contours, _ = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Create complete mask
        final_mask = np.zeros_like(initial_mask)
        for contour in contours:
            # Fill the contours
            cv2.drawContours(final_mask, [contour], -1, (255), -1)
            
        return final_mask