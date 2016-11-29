import csv
from .digraph import Digraph, descendants

SPATH="/home/liren/stash/ngnet/data/wordnet/synsets.txt"
HPATH="/home/liren/stash/ngnet/data/wordnet/hyponyms.txt"
SPATH1="/home/liren/stash/ngnet/test_data/wordnet/synsets1000-subgraph.txt"
HPATH1="/home/liren/stash/ngnet/test_data/wordnet/hyponyms1000-subgraph.txt"
SPATH2="/home/liren/stash/ngnet/test_data/wordnet/synsets14.txt"
HPATH2="/home/liren/stash/ngnet/test_data/wordnet/hyponyms14.txt"


class WordNet:
    """The data structure that stores entire WordNet"""
    def __init__(self, synsets_path, hyponyms_path):
        # v2s: a list of synsets, its indices represent synset vertices
        # s2v: noun -> the synset vertices it belongs to
        self.v2s, self.s2v = [], {}
        #all the unique nouns
        self.all_nouns = []

        with open(synsets_path) as sfile:
            reader = csv.reader(sfile)
            for row in reader:
                words = row[1].split(' ')
                self.v2s.append(words)
                self.all_nouns += words
                for word in words:
                    if word in self.s2v:
                        self.s2v[word].append(int(row[0]))
                    else:
                        self.s2v[word] = [int(row[0])]
        self.all_nouns = set(self.all_nouns)

        # a directed graph of hypernyms pointing to hyponyms
        self.G = Digraph(len(self.v2s))
        with open(hyponyms_path) as hfile:
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
#wn = WordNet(SPATH, HPATH)
#wn.hypnoyms('haemoglobin')
