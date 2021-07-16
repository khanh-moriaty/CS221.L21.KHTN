from nlu.Embedding import Embedding
from .pos_tagging import POS
from .ner_tagging import NER
from .intent_classifier import IntentClassifier
import random
import editdistance
import json
def load_ans(path):
    ans = []
    with open(path ,encoding="utf-8-sig") as _file:
        docs = _file.readlines()
    for sen in docs:
        sen = sen.replace('\n','')
        ans.append(sen)
    return ans

class NLU:
    
    def get_response(self, context, sentence):
        '''
        Generate a response for chatbot based on a target sentence and a context.
        
        Input:
            - context (list of str): a list of previous sentences in our conversation.
            - sentence (str): the sentence/query that user sent to chatbot.
        
        Output (str): a proper response to the user's sentence.
        '''
        
        # Template: Reponse 'You said "sentence"'.
        pos_tag = self.pos_model.predict_POS(sentence)
        ner_tag = self.ner_model.predict_NER(sentence, pos_tag)
        intent = self.intent_model.predict_intent(sentence, pos_tag, ner_tag)
        input = sentence.split()
        if intent==3:
            ans = random.choice(self.ans_greet)
        elif intent==2:
            ans = random.choice(self.ans_bye)
        elif intent==4:
            ans = random.choice(self.ans_kohieu)
        else:
            artist = ""
            k = 0
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-A":
                    artist += str(input[i]).capitalize()
                    k = i+1
                    break
            while ner_tag[k]=="I-A" and k<len(ner_tag):
                artist += " " + str(input[k]).capitalize()
                k += 1
                
            genre = ""
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-G":
                    genre += str(input[i])

            mood = ""
            k = 0
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-M":
                    mood += str(input[i])
                    k = i+1
                    break
            while ner_tag[k]=="I-M" and k<len(ner_tag):
                mood += " " + str(input[k])
                k += 1

            if artist != "":
                res = min(enumerate(self.artists), key=lambda x: editdistance.eval(artist, x[1]))
                artist = str(res[1])
            
            if mood != "":
                res = min(self.moods.items(), key=lambda m: editdistance.eval(mood, min(m[1], key=lambda x: editdistance.eval(mood, x))))
                mood = int(res == "buồn")

            if genre != "":
                res = min(self.genres.items(), key=lambda g: editdistance.eval(genre, min(g[1], key=lambda x: editdistance.eval(genre, x))))
                genre = str(res[0])
            

        return "Intent: {}     NER: {}     POS: {}     {}     {}     {}".format(intent, ner_tag, pos_tag, artist, mood, genre)
        
    def load_model(self):
        '''
        Load ML/DL model for POS tagging, NER tagging and Intent Classifying problem.
        '''
        self.pos_model = POS()
        self.ner_model = NER()
        self.intent_model = IntentClassifier()
        self.embedding_model = Embedding()
        
        self.pos_model.load_POS_model()
        self.ner_model.load_NER_model()
        self.intent_model.load_intent_model()
<<<<<<< HEAD
        self.embedding_model.load_fasttext()
=======

    def load_data(self):
        self.ans_bye = load_ans("dataset/Answer_bye.txt")
        self.ans_greet = load_ans("dataset/Answer_greet.txt")
        self.ans_findsong = load_ans("dataset/Answer_findsong.txt")
        self.ans_notfindsong = load_ans("dataset/Answer_notfindsong.txt")
        self.ans_kohieu = load_ans("dataset/Answer_kohieu.txt")
        self.artists = load_ans("dataset/Singer.txt")
        with open('dataset/Genre.json') as f:
            self.genres = json.load(f)
        with open('dataset/mood.json') as f:
            self.moods = json.load(f)


>>>>>>> master
