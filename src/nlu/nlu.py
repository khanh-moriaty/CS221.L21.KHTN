
from nlu.embedding import Embedding
from .pos_tagging import POS
from .ner_tagging import NER
from .intent_classifier import IntentClassifier
import random
import editdistance
import json
import pandas as pd
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
        ner_tag = self.ner_model.predict_NER(sentence, pos_tag, self.embedding_model)[0]
        intent = self.intent_model.predict_intent(sentence, pos_tag, ner_tag, self.embedding_model)
        input = sentence.split()
        artist = genre = mood = link = ans = preLink = ''
        is_all_O = 1
        for i in ner_tag:
            if i!='O':
                is_all_O = 0
        if intent==0 and is_all_O == 1:
            intent = 4
        if intent==1 and context[:3]==("","",""):
            intent = 4       
        if intent==3:
            ans = random.choice(self.ans_greet)
        elif intent==2:
            ans = random.choice(self.ans_bye)
        elif intent==4:
            ans = random.choice(self.ans_kohieu)
        else:
            k = 0
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-A":
                    artist += str(input[i]).capitalize()
                    k = i+1
                    break
            while k<len(ner_tag) and ner_tag[k]=="I-A":
                artist += " " + str(input[k]).capitalize()
                k += 1
                
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-G":
                    genre += str(input[i])

            k = 0
            for i in range(len(ner_tag)):
                if ner_tag[i]=="B-M":
                    mood += str(input[i])
                    k = i+1
                    break
            while k<len(ner_tag) and ner_tag[k]=="I-M":
                mood += " " + str(input[k])
                k += 1

            if artist != "":
                res = min(enumerate(self.artists), key=lambda x: editdistance.eval(artist, x[1]))
                artist = str(res[1])
            
            if mood != "":
                res = min(self.moods.items(), key=lambda m: editdistance.eval(mood, min(m[1], key=lambda x: editdistance.eval(mood, x))))
                mood = int(res[0] == "buồn")

            if genre != "":
                res = min(self.genres.items(), key=lambda g: editdistance.eval(genre, min(g[1], key=lambda x: editdistance.eval(genre, x))))
                genre = str(res[0])

            if intent==1 and context[:3]!=("","",""):
                artist, mood, genre, preLink = context

            if genre != "":
                if artist != "":
                    try:
                        a = self.list_songs_2[self.list_songs_2["artist"].str.contains(artist)]
                        link = a["link"][random.choice(a[a["genre"].str.contains(genre)].index)]
                        cout=0
                        while link==preLink and cout<10:
                            link = a["link"][random.choice(a[a["genre"].str.contains(genre)].index)]
                            cout+=1
                        if cout==10:
                            ans = random.choice(self.ans_notfindsong)
                        else:
                            ans = random.choice(self.ans_findsong) + " " + link
                    except:
                        ans = random.choice(self.ans_notfindsong)
                else:
                    try:
                        link = self.list_songs_2["link"][random.choice(self.list_songs_2[self.list_songs_2["genre"].str.contains(genre)].index)]
                        cout=0
                        while link==preLink and cout<10:
                            link = self.list_songs_2["link"][random.choice(self.list_songs_2[self.list_songs_2["genre"].str.contains(genre)].index)]
                            cout+=1
                        if cout==10:
                            ans = random.choice(self.ans_notfindsong)
                        else:
                            ans = random.choice(self.ans_findsong) + " " + link
                    except:
                        ans = random.choice(self.ans_notfindsong)
            else:
                if mood != "":
                    if artist != "":
                        try:
                            a = self.list_songs_1[self.list_songs_1["singer"].str.contains(artist)]
                            link = a["link"][random.choice(a[a["mood_binary"]==mood].index)]
                            while link==preLink and cout<10:
                                link = a["link"][random.choice(a[a["mood_binary"]==mood].index)]
                                cout+=1
                            if cout==10:
                                ans = random.choice(self.ans_notfindsong)
                            else:
                                ans = random.choice(self.ans_findsong) + " " + link
                        except:
                            ans = random.choice(self.ans_notfindsong)
                    else:
                        try:
                            link = self.list_songs_1["link"][random.choice(self.list_songs_1[self.list_songs_1["mood_binary"]==mood].index)]
                            while link==preLink and cout<10:
                                link = self.list_songs_1["link"][random.choice(self.list_songs_1[self.list_songs_1["mood_binary"]==mood].index)]
                                cout+=1
                            if cout==10:
                                ans = random.choice(self.ans_notfindsong)
                            else:
                                ans = random.choice(self.ans_findsong) + " " + link
                        except:
                            ans = random.choice(self.ans_notfindsong)
                else:
                    if artist != "":
                        try:
                            link = self.list_songs_1["link"][random.choice(self.list_songs_1[self.list_songs_1["singer"].str.contains(artist)].index)]
                            while link==preLink and cout<10:
                                link = self.list_songs_1["link"][random.choice(self.list_songs_1[self.list_songs_1["singer"].str.contains(artist)].index)]
                                cout+=1
                            if cout==10:
                                ans = random.choice(self.ans_notfindsong)
                            else:
                                ans = random.choice(self.ans_findsong) + " " + link
                        except:
                            ans = random.choice(self.ans_notfindsong)
        return ans, link, ner_tag, pos_tag, intent, artist, mood, genre
        
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
        self.embedding_model.load_fasttext()
        
        self.load_data()

    def load_data(self):
        self.ans_bye = load_ans("/src/dataset/Answer_bye.txt")
        self.ans_greet = load_ans("/src/dataset/Answer_greet.txt")
        self.ans_findsong = load_ans("/src/dataset/Answer_findsong.txt")
        self.ans_notfindsong = load_ans("/src/dataset/Answer_notfindsong.txt")
        self.ans_kohieu = load_ans("/src/dataset/Answer_kohieu.txt")
        self.artists = load_ans("/src/dataset/Singer.txt")
        with open('/src/dataset/Genre.json') as f:
            self.genres = json.load(f)
        with open('/src/dataset/mood.json') as f:
            self.moods = json.load(f)
        self.list_songs_1 = pd.read_csv('/src/dataset/nhaccuatui_v2.csv', usecols=['singer','link','mood_binary'])
        self.list_songs_2 = pd.read_csv('/src/dataset/genre_song.csv', usecols=['artist','genre','link'])
