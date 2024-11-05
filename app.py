import os
import cv2
import sys
import time
import configparser
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from chat import AIChatLibrary
from image_clean_up import ImageCleanUp
from flask import Flask, jsonify, request, render_template, redirect, url_for

# 初始化 Flask 應用程式和所需的類別
app = Flask(__name__)
config = configparser.ConfigParser()

# 全域變數
input_text = ""        # 使用者輸入的文字
input_image = None     # 使用者上傳的圖片
num = 1                # 圖片計數器

def get_admin_account():
    config.read('set/key.ini', encoding='utf-8')
    try:
        account = config['admin-account']['account']
        return account
    except (KeyError, configparser.NoSectionError):
        return None

def get_admin_password():
    
    config.read('set/key.ini', encoding='utf-8')
    try:
        password = config['admin-password']['password']
        return password
    except (KeyError, configparser.NoSectionError):
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_account = get_admin_account()
        admin_password = get_admin_password()
        if admin_password is None or admin_account is None:
            return "無法讀取管理員憑證", 500
            
        username = request.values.get('username')
        password = request.values.get('password')

        if username == admin_account and password == admin_password:
            return redirect(url_for('setting'))
        else:
            return render_template('login.html')
            
    return render_template('login.html')

@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if request.method == 'POST':
        groq_api = request.values.get("groq_api")
        google_api = request.values.get("google_api")
        cse_id = request.values.get("cse_id")
        system_prompt = request.values.get("system_prompt")
        # 新增Grounding with Google Search api
        
        # 寫入設定到 key.ini
        config['groq-api'] = {'api': groq_api}
        config['google-api'] = {'api': google_api}
        config['cse-id'] = {'id': cse_id}
        config['system-prompt'] = {'prompt': system_prompt}
        # 新增Grounding with Google Search api
        
        with open('set/key.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)
            
        return jsonify({"groq_api": groq_api, "google_api": google_api, "cse_id": cse_id, "system_prompt": system_prompt}), 200
    else:
        return render_template('setting.html')

@app.route('/ai-api/text', methods=['POST'])
def upload_data():
    global input_text, input_image
    
    # 取得請求中的 JSON 資料
    data = request.json
    
    

if __name__ == '__main__':
    app.run(debug=True)
