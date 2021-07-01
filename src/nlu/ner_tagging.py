


class NER:
    
    def predict_NER(self, sentence, pos_tag):
        '''
        Predict NER tagging of a sentence.
        
        Input:
            - sentence (str): the input sentence that needs to be processed.
            - pos_tag (list of str): POS tagging for the input sentence.
            
        Output (list of str): a list with the same length as sentence, 
        where i-th element is the NER tagging of i-th word in the input sentence.
        '''
        
        # Template: Predict "O" tag for all words.
        return ['O'] * len(sentence.split())
    
    def load_NER_model(self):
        self.model = ...