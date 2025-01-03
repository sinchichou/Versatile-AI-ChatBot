import configparser
import requests
import json
import set.set
import re
from datetime import datetime
from requests import *
from groq import Groq
import onnxruntime as ort
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

config = configparser.ConfigParser()

class AIChatLibrary:
    def __init__(self, groq_api):
        config.read('set/key.ini', encoding='utf-8')
        self.system_prompt = config['system-prompt']['prompt']
        self.chat_model = config['chat-model']['model']
        self.client = Groq(api_key=groq_api)  
        self.google_api = config['google-api']['api']
        self.cse_id = config['cse-id']['id']
        return self

    def chat_online_model(self, input_text, text_list):
        chat = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.system_prompt + input_text + "".join(text_list),
                }
            ],
            model=self.chat_model,
            max_tokens=8192,
        )
        return chat.choices[0].message.content

    # locat LLM 
    # using ONNX --> GPU
    # input  --> input_text
    # output --> output_text
    def chat_locat(self, input_text):
        session = ort.InferenceSession("model.onnx")
        inputs = {"input_name": input_text}
        output_text = session.run(None, inputs)
        return output_text
    
    def transformers2onnx():
        model_checkpoint = "distilbert_base_uncased_squad"  # download model transformers to onnx

        # Load a model from transformers and export it to ONNX
        ort_model = ORTModelForSequenceClassification.from_pretrained(model_checkpoint, export=True)
        tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

        # Save the onnx model and tokenizer
        ort_model.save_pretrained(save_directory)
        tokenizer.save_pretrained(save_directory)
    
    def log(self, reply):
        with open('example.txt', 'w', encoding='utf-8') as file:
            file.write(reply + "\n\n")

    def google_search(self, query):
        """
        Use Google Custom Search Engine to search and download relevant webpage content.
        """
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.google_api,
            'cx': self.cse_id,
            'q': query
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json().get('items', [])
            links = [item['link'] for item in results]

            # Download the content of each URL
            contents = []
            for link in links:
                content = self.get_webpage(link)
                contents.append(content)
            return contents

        except requests.RequestException as e:
            print(f"Search request failed: {e}")
            return []

    def get_webpage(self, url):
        """
        Get the content of the specified URL.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Unable to download webpage content: {e}")
            return ""
    # need to fix
    # the keywords list need to updata and add more
    # need to add the download function
    
    @staticmethod
    def needs_search(query, knowledge_cutoff_date, current_date):
        """
        Determine if a search is needed.
        """
        # 1. Check if real-time information is mentioned
        if any(keyword in query.lower() for keyword in ['現在', '即時', '今天', '目前']): # need to add 12/7
            return True

        # 2. Check if a specific date is mentioned and if it exceeds the knowledge cutoff date
        date_patterns = [r'\d{4}[-/]\d{1,2}[-/]\d{1,2}', r'\b\d{1,2}月\d{1,2}日\b']
        for pattern in date_patterns:
            match = re.search(pattern, query)
            if match:
                try:
                    # Try to parse the date
                    query_date = datetime.strptime(match.group(), "%Y-%m-%d")
                    if query_date > knowledge_cutoff_date:
                        return True
                except ValueError:
                    pass  # Ignore if the date format cannot be parsed

        # 3. Check for unknown terms or proper nouns
        unknown_keywords = ['新技術', '最新工具', '未定義詞']
        if any(keyword in query.lower() for keyword in unknown_keywords):
            return True

        # 4. If it is unrelated to knowledge but mentions websites or needs to download
        if any(keyword in query.lower() for keyword in ['下載', '網頁', '網站', '連結']):
            return True

        # Default to not needing a search
        return False
    
    # Define data time 
    knowledge_cutoff_date = datetime(2023, 10, 1)  # Model training cutoff date. for check the Groq API model list, on app.py function "get_groq_models_list"
    current_date = datetime.now()
