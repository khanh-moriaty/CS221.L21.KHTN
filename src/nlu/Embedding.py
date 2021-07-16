import fasttext
import fasttext.util
import numpy as np

class Embedding:

    def load_fasttext(self):
        self.model = fasttext.load_model('/src/nlu/cc.vi.300.bin')

    def get_embedding(self, word):
        word=word.lower()
        try:
            vector=self.model[word]
        except:
            # if the word is not in vocabulary,
            # returns zeros array
            vector=np.zeros(300,)

        return vector 