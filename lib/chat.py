import configparser
import google.generativeai as genai
from googleapiclient.discovery import build
from groq import Groq

config = configparser.ConfigParser()

class AIChatLibrary:

    def get_set(self):          
        config.read('set/key.ini', encoding='utf-8')
        self.groq_api = config['groq-api']['api']
        self.google_api = config['google-api']['api']
        self.cse_id = config['cse-id']['id']
        self.system_prompt = config['system-prompt']['prompt']
        self.client = Groq(api_key=self.groq_api)  # 在這裡新增 client
        # 新增Grounding with Google Search api
        return self.groq_api, self.google_api, self.cse_id, self.system_prompt

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
    def google_search(self, input_text):
        model = genai.GenerativeModel('models/gemini-1.5-pro-002')
        google_search_response = model.generate_content(
            contents=input_text,
            tools={"google_search_retrieval": {
                    "dynamic_retrieval_config": {
                    "mode": "unspecified",
                    "dynamic_threshold": 0.06}}})
        return google_search_response

    def log(self, reply):
        with open('example.txt', 'w', encoding='utf-8') as file:
            file.write(reply + "\n\n")
