

import os
import string
import numpy as np
import pickle
import underthesea
import fasttext
bad_chars = [';', ':', '!', "*", "-",".",",","%","(",")","/","{","}","[","]"]
bad_words = ['nhé', 'nha', 'nhe', 'ha', 'nhen', 'he', 'hen', 'đi']

def softmax(Z):
    e_Z = np.exp(Z)
    A = e_Z / e_Z.sum(axis = 0)
    return A

def pred(W, X):
    A = softmax(W.T.dot(X))
    return A

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
        test_array = np.array([vec])
        temp = test_array.T
        K = np.concatenate((np.ones((1, len(test_array))), temp), axis = 0)
        T = pred(self.model, K)
        tem = np.argmax(T, axis = 0)
        return tem[0]
        
    def load_intent_model(self):
         #dowload here https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.bin.gz
        self.ft = fasttext.load_model('cc.vi.300.bin')
        self.model = pickle.load(open('/src/nlu/model/clf_model/final_model_new_v2.sav','rb'))

    def predict_1sen(self, sen):
        vec = np.zeros((300, ), dtype='float32')
        words_arr_1sen = underthesea.word_tokenize(sen, format="text").split()
        n = len(words_arr_1sen)
        for word in words_arr_1sen:
            if word in bad_chars:
                n -= 1
                continue
            if word in bad_words:
                n -= 1
                continue
            try:
                temp = self.ft.get_word_vector(word)
                #tong = sum(temp)
                #norm = [float(i)/tong for i in temp]
                vec += temp            
            except:
                n -= 1
        if n>0:
            vec = np.divide(vec, n)
        return vec

# a = IntentClassifier()
# a.load_intent_model()
# print(a.predict_intent("xin chào","",""))
