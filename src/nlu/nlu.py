from .pos_tagging import POS
from .ner_tagging import NER
from .intent_classifier import IntentClassifier

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
        return "Intent: {}\nNER: {}\nPOS: {}".format(intent, ner_tag, pos_tag)
        
    def load_model(self):
        '''
        Load ML/DL model for POS tagging, NER tagging and Intent Classifying problem.
        '''
        self.pos_model = POS()
        self.ner_model = NER()
        self.intent_model = IntentClassifier()
        
        self.pos_model.load_POS_model()
        self.ner_model.load_NER_model()
        self.intent_model.load_intent_model()
