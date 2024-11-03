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
        初始化 ImageCleanUp 類別
        使用 lama-cleaner 進行圖片修復
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = LaMa(device=self.device)

    def process_image(self, image_data):
        """
        處理圖片並移除粉色區域
        
        參數:
            image_data: 二進制圖片資料
            
        回傳:
            inpainted_result: 修復後的圖片
        
        使用範例:
            from image_clean_up import ImageCleanUp
            
            # 初始化類別
            cleaner = ImageCleanUp()
            
            # 讀取圖片
            with open('image.jpg', 'rb') as f:
                image_data = f.read()
                
            # 處理圖片
            result = cleaner.process_image(image_data)
            
            # 儲存結果
            cv2.imwrite('result.jpg', result)
        """
        # 將圖片資料轉換為OpenCV格式
        nparr = np.frombuffer(image_data, np.uint8)
        self.img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # 生成遮罩
        mask = self.create_mask_from_pink()
        
        # 使用 lama-cleaner 進行修復
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
        從圖片中識別粉色區域並創建遮罩
        
        回傳:
            final_mask: 粉色區域的遮罩
        """
        # 轉換到HSV色彩空間
        hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        
        # 定義亮粉色的範圍
        lower_pink = np.array([140, 100, 100])
        upper_pink = np.array([180, 255, 255])
        
        # 創建初始遮罩
        initial_mask = cv2.inRange(hsv_img, lower_pink, upper_pink)
        
        # 使用形態學運算擴展遮罩區域
        kernel = np.ones((5,5), np.uint8)
        dilated_mask = cv2.dilate(initial_mask, kernel, iterations=2)
        
        # 尋找連通區域
        contours, _ = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 創建完整遮罩
        final_mask = np.zeros_like(initial_mask)
        for contour in contours:
            # 填充輪廓
            cv2.drawContours(final_mask, [contour], -1, (255), -1)
            
        return final_mask