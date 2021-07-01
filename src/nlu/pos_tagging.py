


class POS:
        
    def predict_POS(self, sentence):
        '''
        Predict POS tagging of a sentence.
        
        Input:
            - sentence (str): the input sentence that needs to be processed.
            
        Output (list of str): a list with the same length as sentence, 
        where i-th element is the POS tagging of i-th word in the input sentence.
        '''
        
        # Template: Predict "N" tag for all words.
        return ['N'] * len(sentence.split())
    
    def load_POS_model(self):
        self.model = ...