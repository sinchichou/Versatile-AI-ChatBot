import os 
import requests
import torch
import onnxruntime as ort

class ModelManager:
    def __init__(self, model_path):
        self.HF_API_URL = "https://huggingface.co/api/models"
        self.MODEL_PATH = "./model/"


    def fetch_models(self, query="text-generation"):
        params = {"filter": query}
        response = requests.get(self.HF_API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return []
