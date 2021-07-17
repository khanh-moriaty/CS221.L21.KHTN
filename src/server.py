from flask import Flask, request
from flask_cors import CORS
import time
import secrets

app = Flask(__name__)
CORS(app)

from nlu import NLU

# Initialize NLU module
nlu = NLU()
nlu.load_model()

@app.route("/frontend/message", methods=["GET", "POST"])
def frontend_message():
    receive_time = int(time.time() * 1000)
    
    if request.method == "GET":
        return {
            'token': secrets.token_hex(),
            'messages': [
                {
                    'username': 'CHATBOT',
                    'timestamp': receive_time,
                    'message': "Xin chào! Mình là Chatbot thông minh vjp pro có chức năng gợi ý bài hát. \
                        Bạn hãy nhập câu hỏi vào khung chat bên dưới để bắt đầu giao tiếp nhé!",
                },
            ],
        }
    
    try:
        content = request.get_json()
        token = content['token']
        message = content['message']
        
        # Process user input
        response = nlu.get_response(context=[], sentence=message)
        
        response_time = int(time.time() * 1000)
        return {
            'token': token,
            'messages': [
                {
                    'username': 'YOU',
                    'timestamp': receive_time,
                    'message': message,
                },
                {
                    'username': 'CHATBOT',
                    'timestamp': response_time,
                    'message': response,
                },
            ],
        }
    except:
        return {
            'token': token,
            'messages': [
                {
                    'username': 'YOU',
                    'timestamp': receive_time,
                    'message': message,
                },
                {
                    'username': 'CHATBOT',
                    'timestamp': receive_time,
                    'message': "Oops! Có lỗi xảy ra rồi :(",
                },
            ],
        }

@app.route("/webhook/message", methods=["GET", "POST"])
def webhook_message():
    pass
    # """This is the main function flask uses to 
    # listen at the `/webhook` endpoint"""
    # if request.method == 'GET':
    #     return verify_webhook(request)

    # if request.method == 'POST':
    #     payload = request.json
    #     print(payload)
    #     event = payload['entry'][0]['messaging']
    #     for x in event:
    #         if is_user_message(x):
    #             text = x['message']['text']
    #             sender_id = x['sender']['id']
    #             respond(sender_id, text)

    #     return "ok"
