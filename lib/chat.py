import configparser
from groq import Groq

config = configparser.ConfigParser()

class AIChatLibrary:
    def get_set(self, groq_api):          
        config.read('set/key.ini', encoding='utf-8')
        self.system_prompt = config['system-prompt']['prompt']
        self.chat_model = config['chat-model']['model']
        self.client = Groq(api_key=groq_api)  
        return self
    
    # 製作計畫
    # def making_todo(self, input_text):
    #     making_todo = self.client.chat.completions.create(
    #         messages=[
    #             {
    #                 "role": "user",
    #                 "content": "1. Create a problem-solving process 2. Develop a solution plan" + {input_text},
    #             }
    #         ],
    #         model="gemma-7b-it",
    #         max_tokens=8192,
    #     )
    #     return making_todo.choices[0].message.content

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
