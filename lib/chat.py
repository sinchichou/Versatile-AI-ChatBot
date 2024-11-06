import configparser
import requests
from groq import Groq

config = configparser.ConfigParser()

class AIChatLibrary:

    def get_set(self):          
        config.read('set/key.ini', encoding='utf-8')
        self.groq_api = config['groq-api']['api']
        self.google_api = config['google-api']['api']
        self.cse_id = config['cse-id']['id']
        self.system_prompt = config['system-prompt']['prompt']
        self.client = Groq(api_key=self.groq_api)  
        self.Grounding_Google_Search_api = config['Grounding_Google_Search_api']['api']
        self.temperture = config['Google-Search-ai']['temperature']
        self.topK = config['Google-Search-ai']['topK']
        self.topP = config['Google-Search-ai']['topP']
        self.maxOutputTokens = config['Google-Search-ai']['maxOutputTokens']
        return self 
        #.groq_api, self.google_api, self.cse_id, self.system_prompt, self.Grounding_Google_Search_api, self.temperture   
    
    def making_todo(self, input_text):
        making_todo = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "1. Create a problem-solving process 2. Develop a solution plan" + {input_text},
                }
            ],
            model="gemma-7b-it",
            max_tokens=8192,
        )
        return making_todo.choices[0].message.content

    def chat(self, todo_sept, input_text, text_list):
        chat = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self.system_prompt + todo_sept + input_text + "".join(text_list),
                }
            ],
            model="llama-3.2-90b-vision-preview",
            max_tokens=8192,
        )
        return chat.choices[0].message.content

    # 使用Grounding with Google Search生成回答
    def google_search(self, input_text, temperature, topK, topP, maxOutputTokens):
        # 設定 API_KEY 和請求 URL
        API_KEY = "YOUR_API_KEY"  # 請將此處替換為您的實際 API 金鑰
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-002:generateContent?key={API_KEY}"

        # 設定請求的內容資料
        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": input_text  # 使用輸入文字
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": temperature,  # 調整生成內容的隨機性
                "topK": topK,         # 限制考慮的最高概率的詞彙數量
                "topP": topP,        # 使用核取樣來控制生成的多樣性
                "maxOutputTokens": maxOutputTokens,  # 限制生成的最大字元數
                "responseMimeType": "application/json"  # 設定回應的 MIME 類型
            }
        }

        # 設定 headers
        headers = {
            "Content-Type": "application/json"
        }

        # 發送 POST 請求
        response = requests.post(url, headers=headers, json=data)

        # 檢查回應是否成功
        if response.status_code == 200:
            return response.json()
        else:
            print("無法獲取資料。狀態碼:", response.status_code)
            print("錯誤:", response.text)
            return None



    def log(self, reply):
        with open('example.txt', 'w', encoding='utf-8') as file:
            file.write(reply + "\n\n")
