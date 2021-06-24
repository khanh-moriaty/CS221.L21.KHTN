from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/frontend/message", methods=["GET", "POST"])
def frontend_message():
    receive_time = int(time.time() * 1000)
    
    content = request.get_json()
    token = content['token']
    message = content['message']
    
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
                'message': 'You said "{}"'.format(message),
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
