


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
        return 0
    
    def load_intent_model(self):
        self.model = ...