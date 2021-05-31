from utilities import *

import re
import os
import json
import itertools
from utils.trie import Trie
from multiprocessing import Pool

class NGrams():

    def __init__(self, corpus_dir):
        self.corpus_dir = [os.path.join(corpus_dir, x) for x in os.listdir(corpus_dir)]
    
    def import_ngrams(self, inp_file, n=1):
        self.ngrams = Trie()._import(inp_file)
        self.n = n
    
    def _generate_ngrams(self, corpus_file, n=1):
        '''
        Generate n-grams language model for a corpus.
        
        Parameters:
            - corpus_file: path to a corpus file.
            - n: number of consective words to be recorded by n-grams.
            
        Returns: Trie object representing the n-grams language model.
        '''
        
        ngrams = Trie()
        
        with open(corpus_file, encoding='utf-8') as corpus:
            for i, sentence in enumerate(corpus):
                # if i % 1000000 == 0:
                #     print(i)
                # if i > 1000000: break
                orig_sentence = sentence
                sentence = sentence.strip()
                sentence = re.sub('[^ {}]'.format(VN_ALPHABETS), ' ', sentence)
                sentence = re.sub('  ', ' ', sentence)
                sentence = sentence.lower()
                sentence = sentence.split()
                for i in range(len(sentence)-n+1):
                    ngram = ' '.join(sentence[i:i+n])
                    ngrams.add(ngram)
        
        return ngrams

    def generate_ngrams(self, n=1, subprocess=32):
        '''
        Generate n-grams language model for corpus directory specified in the constructor.
        This utilizes multiprocessing for faster computing.
        
        Parameters:
            - n: number of consective words to be recorded by n-grams.
            - subprocess: number of processes to be used by this function.
            
        Returns: Trie object representing the n-grams language model for all corpus files.
        '''
        
        with Pool(subprocess) as pool:
            ngrams = pool.starmap(self._generate_ngrams, zip(self.corpus_dir, itertools.repeat(n)))
        print('Done processing. Begin merging.')
        self.ngrams = Trie()
        self.n = n
        for ngram in ngrams:
            self.ngrams.merge(ngram)
        return self.ngrams
    
    def _export_ngrams(self, out_file, n=1):
        self.generate_ngrams(n)._export(out_file)
    
    def export_unigrams(self, out_file='/dataset/unigrams_trie.json'):
        self._export_ngrams(out_file, n=1)
    
    def export_bigrams(self, out_file='/dataset/bigrams_trie.json'):
        self._export_ngrams(out_file, n=2)
    
    def export_trigrams(self, out_file='/dataset/trigrams_trie.json'):
        self._export_ngrams(out_file, n=3)
    
if __name__ == '__main__':
    ngrams = NGrams('/dataset/corpus-news')
    ngrams.export_unigrams()