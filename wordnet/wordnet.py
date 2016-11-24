import numpy as np
import pandas as pd
import csv
from digraph import Digraph, descendants

SPATH="../data/wordnet/synsets1000-subgraph.txt"
HPATH="../data/wordnet/hyponyms1000-subgraph.txt"
SCLEAN="../data/synsets_ready.csv"
HCLEAN="../data/hyponyms_ready.csv"

class WordNet:
    """The data structure that stores entire WordNet"""
    def __init__(self, synsets_path, hyponyms_path):
        pp = pd.read_csv(synsets_path, index_col=0)
        # vertex to string set
        self.v2s = pp['synset'].apply(lambda x: set(x.split(' ')))
        # string to vertex set
        self.s2v = {}
        #all the unique nouns
        self.all_nouns = set()
        for id in range(self.v2s.size):
            row = self.v2s[id]
            self.all_nouns = self.all_nouns.union(row)
            for word in row:
                if word in self.s2v:
                    self.s2v[word].add(id)
                else:
                    self.s2v[word] = {id}
        # a directed graph of hypernyms pointing to hyponyms
        self.G = Digraph(self.v2s.size)
        with open(HPATH) as hfile:
            reader = csv.reader(hfile)
            for row in reader:
                for v in row[1:]:
                    self.G.add_edge(int(row[0]), int(v))

    def contains(self, word):
        """Return true if the word is in the WordNet"""
        return word in self.all_nouns

    def nouns(self):
        """Return all nouns"""
        return self.all_nouns

    def hypnoyms(self, word):
        """
        Return hypnoyms as well as synonyms of the word.
        If the word belongs to multiple synsets,
        return all the hypnoyms of these synsets.
        """
        words = set()
        hyponym_ids = descendants(self.G, self.s2v[word])
        for id in hyponym_ids:
            words = words.union(self.v2s[id])
        return words

# test
wn = wordnet.WordNet(wordnet.SCLEAN, wordnet.HPATH)
wn.hypnoyms('haemoglobin')
