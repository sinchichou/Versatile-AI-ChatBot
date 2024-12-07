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

# Initialize Flask application and required classes
app = Flask(__name__)
config = configparser.ConfigParser()

# Global variables
input_text = ""        # User input text
input_image = None     # User uploaded image
num = 1                # Image counter

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
            return {"message":"Unable to read admin credentials"}, 500
            
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
        # Get model list and send to webpage
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
    # Write settings to key.ini
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
                           message="Settings have been saved!"), 200

    # return jsonify({"groq_api": groq_api, 
    #                     "google_api": google_api, 
    #                     "cse_id": cse_id, 
    #                     "system_prompt": system_prompt, 
    #                     "chat_model": chat_model, 
    #                     }), 200

@app.route('/ai-api/text', methods=['POST'])
def upload_data():
    global input_text
    # Get JSON data from the request
    if request.method == 'POST':
        admin_account = get_admin_account()
        admin_password = get_admin_password()
        if admin_password is None or admin_account is None:
            return {"message": "Account or password cannot be read"}, 500
        account = request.values.get('account')
        password = request.values.get('password')
        if account != admin_account or password != admin_password:
            return {"message": "Account or password error"}, 401  # 401 indicates unauthorized
        input_text = request.values.get('text')
        # print(input_text)
    return {"message":"Success", 
            "input_text":input_text}, 200

if __name__ == '__main__':
    app.run(debug=True)
