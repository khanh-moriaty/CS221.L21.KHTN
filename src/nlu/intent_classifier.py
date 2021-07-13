import gensim

from gensim.models import KeyedVectors

import os
import string
import numpy as np
import pickle

bad_chars = [';', ':', '!', "*", "-",".",",","%","(",")","/","{","}","[","]"]
class IntentClassifier:
    
    def predict_intent(self, sentence, pos_tag, ner_tag):
        '''
        Classify the chatbot intent of an input sentence based on its content, 
        its corresponding POS tags and NER tags.
        
        Input:
            - sentence (str): the input sentence that needs to be processed.
            - pos_tag (list of str): POS tagging for the input sentence.
            - pos_tag (list of str): NER tagging for the input sentence.
            
        Output (int): intent class of the input sentence.
        '''
        
        # Template: always return class 0.
        vec = np.array(self.predict_1sen(sentence))
        y_pred = self.model.predict([vec])
        return y_pred[0]

    def load_intent_model(self):
        w2vmodel = "/src/nlu/wiki.vi.model.bin" #dowload here https://thiaisotajppub.s3-ap-northeast-1.amazonaws.com/publicfiles/wiki.vi.model.bin.gz
        self.w2v_model = KeyedVectors.load_word2vec_format(w2vmodel, binary=True)
        self.model = pickle.load(open('/src/nlu/model/clf_model/final_model.sav','rb'))
    def predict_1sen(self, sen):
        sentence = [word for word in sen.lower().split()]
        print('Sentences:', sentence)
        vec = np.zeros((400, ), dtype='float32')
        n = len(sentence)
        for word in sentence:
            for j in bad_chars:
                word = word.replace(j, ' ')
            try:
                vec = self.w2v_model[word]
            except:
                n -= 1
        if n>0:
            vec = np.divide(vec, n)
        return vec

# a = IntentClassifier()
# a.load_intent_model()
# print(a.predict_intent("xin chào","",""))