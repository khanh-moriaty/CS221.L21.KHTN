from underthesea import pos_tag

class POS:
        
    def predict_POS(self, sentence):
        '''
        Predict POS tagging of a sentence.
        
        Input:
            - sentence (str): the input sentence that needs to be processed.
            
        Output (list of str): a list with the same length as sentence, 
        where i-th element is the POS tagging of i-th word in the input sentence.
        '''
        pos = pos_tag(sentence)
        pos = [list(x) for x in pos]
        newpos = []
        for po in pos:
            if len(po[0].split()) > 1:
                for i in po[0].split():
                    newpos.append(po[1])
            else:
                newpos.append(po[1])

        # Template: Predict "N" tag for all words.
        return newpos
    
    def load_POS_model(self):
        self.model = ...