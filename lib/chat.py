import configparser
import requests
from requests import *
from groq import Groq
from scrapling import Fetcher, StealthyFetcher, PlayWrightFetcher

config = configparser.ConfigParser()

class AIChatLibrary:
    def get_set(self, groq_api):          
        config.read('set/key.ini', encoding='utf-8')
        self.system_prompt = config['system-prompt']['prompt']
        self.chat_model = config['chat-model']['model']
        self.client = Groq(api_key=groq_api)  
        self.google_api = config['google-api']['api']
        self.cse_id = config['cse-id']['id']
        return self

    def chat(self, input_text, text_list):
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

    def log(self, reply):
        with open('example.txt', 'w', encoding='utf-8') as file:
            file.write(reply + "\n\n")

    # def google_search(self, query):
    #     url = "https://www.googleapis.com/customsearch/v1"
    #     params = {
    #         'key': self.google_api,  # 替換為你的API金鑰
    #         'cx': self.cse_id,     # 替換為你的自定義搜尋引擎ID
    #         'q': query
    #     }
    #     response = requests.get(url, params=params)
    #     results = response.json().get('items', [])
    #     return [item['link'] for item in results]

    def search(self, query):
        url = "https://www.google.com/search?"
        q_key = query
        default_key = "&sourceid=chrome&ie=UTF-8"
        page = StealthyFetcher().fetch(url=f"{url}q={q_key}{default_key}")
        page.find_all('div', id_="search")
        
