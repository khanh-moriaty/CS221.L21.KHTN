import pickle
 
class NER:
    
    def word2features(self, sent, i):
        word = sent[i][0]
        postag = sent[i][1]

        features = {
            'bias': 1.0,
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word[-2:]': word[-2:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'postag': postag,
            'postag[:2]': postag[:2],
        }
        if i > 0:
            word1 = sent[i-1][0]
            postag1 = sent[i-1][1]
            features.update({
                '-1:word.lower()': word1.lower(),
                '-1:word.istitle()': word1.istitle(),
                '-1:word.isupper()': word1.isupper(),
                '-1:postag': postag1,
                '-1:postag[:2]': postag1[:2],
            })
        else:
            features['BOS'] = True

        if i < len(sent)-1:
            word1 = sent[i+1][0]
            postag1 = sent[i+1][1]
            features.update({
                '+1:word.lower()': word1.lower(),
                '+1:word.istitle()': word1.istitle(),
                '+1:word.isupper()': word1.isupper(),
                '+1:postag': postag1,
                '+1:postag[:2]': postag1[:2],
            })
        else:
            features['EOS'] = True

        return features

    def sent2features(self, sent):
        return [self.word2features(sent, i) for i in range(len(sent))]

    def load_NER_model(self):
        self.model = pickle.load(open('/CS221.L21.KHTN/NER_model/final_model.sav','rb'))

    def predict_NER(self, sentence, pos_tag):
        '''
        Predict NER tagging of a sentence.
        
        Input:
            - sentence (str): the input sentence that needs to be processed.
            - pos_tag (list of str): POS tagging for the input sentence.
            
        Output (list of str): a list with the same length as sentence, 
        where i-th element is the NER tagging of i-th word in the input sentence.
        '''

        data = []
        sentence = sentence.split()
        for i in range(len(sentence)):
            data.append([sentence[i], pos_tag[i]])
        X_test = [self.sent2features(data)]
        y_pre = self.model.predict(X_test)
        # Template: Predict "O" tag for all words.
        return y_pre
    
    