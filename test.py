import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from chat import AIChatLibrary

def set_parameters():
    input_text = "台灣近期的颱風"
    temperature = 0.7
    topK = 40
    topP = 0.95
    maxOutputTokens = 1024
    api = ""
    return input_text, temperature, topK, topP, maxOutputTokens, api

input_text, temperature, topK, topP, maxOutputTokens, api = set_parameters()

ai_chat_library = AIChatLibrary()  # 實例化 AIChatLibrary
# ai_chat_library.get_set()  # 確保配置已加載
r_t = ai_chat_library.google_search(input_text=input_text, temperature=temperature, topK=topK, topP=topP, maxOutputTokens=maxOutputTokens, Grounding_Google_Search_api=api)

print(r_t)