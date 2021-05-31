from utilities import *

import re
import os
import json
import itertools
from collections import Counter
from multiprocessing import Pool

class NGrams():

    def __init__(self, corpus_dir):
        self.corpus_dir = [os.path.join(corpus_dir, x) for x in os.listdir(corpus_dir)]
    
    def import_ngrams(self, inp_file, n=1):
        with open(inp_file) as fi:
            self.ngrams = json.load(fi)
            self.n = n
    
    def import_mapping(self, inp_file):
        with open(inp_file) as fi:
            self.mapping = json.load(fi)
            
    def _map(self, ngram):
        power = 1
        res = 0
        for i, x in enumerate(reversed(ngram.split())):
            res += power + self.mapping[x]
            power *= len(self.mapping)
        return res
    
    def _generate_ngrams(self, corpus_file, n=1):
        '''
        Generate n-grams language model for a corpus.
        
        Parameters:
            - corpus_file: path to a corpus file.
            - n: number of consective words to be recorded by n-grams.
            
        Returns: Counter object representing the n-grams language model.
        '''
        
        ngrams = Counter()
        
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
                    ngrams[ngram] += 1
        
        return ngrams

    def generate_ngrams(self, n=1, subprocess=30):
        '''
        Generate n-grams language model for corpus directory specified in the constructor.
        This utilizes multiprocessing for faster computing.
        
        Parameters:
            - n: number of consective words to be recorded by n-grams.
            - subprocess: number of processes to be used by this function.
            
        Returns: Counter object representing the n-grams language model for all corpus files.
        '''
        
        with Pool(subprocess) as pool:
            ngrams = pool.starmap(self._generate_ngrams, zip(self.corpus_dir, itertools.repeat(n)))
        self.ngrams = Counter()
        self.n = n
        for ngram in ngrams:
            self.ngrams += ngram
        return self.ngrams
    
    def _export_ngrams(self, out_file, n=1):
        ngrams = self.generate_ngrams(n)
        with open(out_file, 'w') as fo:
            json.dump(ngrams, fo)
    
    def export_unigrams(self, out_file='/dataset/unigrams.json'):
        self._export_ngrams(out_file, n=1)
    
    def export_bigrams(self, out_file='/dataset/bigrams.json'):
        self._export_ngrams(out_file, n=2)
    
    def export_trigrams(self, out_file='/dataset/trigrams.json'):
        self._export_ngrams(out_file, n=3)
    
if __name__ == '__main__':
    ngrams = NGrams('/dataset/corpus-news')
    ngrams.export_unigrams()