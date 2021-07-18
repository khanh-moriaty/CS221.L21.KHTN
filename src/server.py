from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo
import time
import secrets
import os
import traceback

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = 'mongodb://' + \
                            os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + \
                            os.environ['MONGO_INITDB_ROOT_PASSWORD'] + '@' + \
                            'db:27017/musicbot?authSource=admin'
mongo = PyMongo(app)
db = mongo.db

from nlu import NLU

# Initialize NLU module
nlu = NLU()
nlu.load_model()

@app.route("/frontend/message", methods=["GET", "POST"])
def frontend_message():
    receive_time = int(time.time())
    
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
        
        # Get most recent message with NER and (intent==0)
        result = list(db.data.find({
            'token': token, 
            'intent': 0, 
            '$or': [
                {'artist': {'$exists': True, '$ne': ""}},
                {'mood': {'$exists': True, '$ne': ""}},
                {'genre': {'$exists': True, '$ne': ""}},
            ]
        }, sort=[('timestamp', -1)]))
        if result:
            prevArtist = result[0]['artist']
            prevMood = result[0]['mood']
            prevGenre = result[0]['genre']
            prevLink = result[0]['url']
        else:
            prevArtist = ""
            prevMood = ""
            prevGenre = ""
            prevLink = ""
        
        # Process user input
        response, link, ner, pos, intent, artist, mood, genre = nlu.get_response(context=(prevArtist, prevMood, prevGenre, prevLink), sentence=message)
        
        response_time = int(time.time())
        response = {
            'token': token,
            'timestamp': response_time,
            'intent': intent,
            'artist': artist,
            'mood': mood,
            'genre': genre,
            'ner': ner,
            'pos': pos,
            'url': link,
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
                    'url': link,
                },
            ],
        }
        db.data.insert_one(response)
        del response['_id']
        return response
    except Exception as e:
        response = {
            'token': token,
            'timestamp': receive_time,
            'intent': 4,
            'artist': '',
            'mood': '',
            'genre': '',
            'ner': [],
            'pos': [],
            'url': '',
            'error': traceback.format_exc(),
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
        db.data.insert_one(response)
        del response['_id']
        # del response['error']
        return response

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
