import os
import sys
import configparser
import requests
import os
import json
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

def get_groq_models_list():
    groq_api = config['groq']['api']
    url = "https://api.groq.com/openai/v1/models"

    headers = {
        "Authorization": f"Bearer {groq_api}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    result_list = [{"id": model["id"], "owned_by": model["owned_by"], "active": model["active"]} for model in response.json()["data"]]
    return result_list

@app.route('/')
def index():    
    return redirect(url_for('login'))


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
    if request.method != 'POST':
        # 取得模型列表並傳送到網頁
        config.read('set/key.ini', encoding='utf-8')
        groq_api = config['groq']['api']
        if groq_api == "":
            return render_template('setting.html')
        result_list = get_groq_models_list()
        return render_template('setting.html', models=result_list)
    
    admin_account = get_admin_account()
    admin_password = get_admin_password()
    groq_api = request.values.get("groq_api")
    google_api = request.values.get("google_api")
    cse_id = request.values.get("cse_id")
    chat_model = request.values.get("chat_model")
    system_prompt = request.values.get("system_prompt")
    # 寫入設定到 key.ini
    config['google-api'] = {'api': google_api}
    config['cse-id'] = {'id': cse_id}
    config['system-prompt'] = {'prompt': system_prompt}
    config['admin-account'] = {'account': admin_account}
    config['admin-password'] = {'password': admin_password}

    if chat_model != "":
        config['chat-model'] = {'model': str(chat_model)}

    if groq_api != "":
        config['groq-api'] = {'api': groq_api}
        config['groq'] = {'api': groq_api}


    with open('set/key.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
            
    return render_template('setting.html', 
                           groq_api=groq_api, 
                           google_api=google_api, 
                           cse_id=cse_id, 
                           system_prompt=system_prompt, 
                           chat_model=chat_model, 
                           message="設定已儲存！"), 200

    # return jsonify({"groq_api": groq_api, 
    #                     "google_api": google_api, 
    #                     "cse_id": cse_id, 
    #                     "system_prompt": system_prompt, 
    #                     "chat_model": chat_model, 
    #                     }), 200

# need to fix
@app.route('/ai-api/text', methods=['POST'])
def upload_data():
    global input_text
    # 取得請求中的 JSON 資料
    if request.method == 'POST':
        admin_account = get_admin_account()
        admin_password = get_admin_password()
        if admin_password is None or admin_account is None:
            return "account or password can not benn read", 500
        account = request.values.get('account')
        password = request.values.get('password')  
        if account != admin_account and password != admin_password:
            return "account or password error"
        input_text = request.values.get('qution')
        print(input_text)
    return 200

if __name__ == '__main__':
    app.run(debug=True)
