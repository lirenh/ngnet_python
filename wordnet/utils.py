import numpy as np
import pandas as pd

SPATH="../data/wordnet/synsets1000-subgraph.txt"
HPATH="../data/wordnet/hyponyms1000-subgraph.txt"
SCLEAN="../data/synsets_ready.csv"
HCLEAN="../data/hyponyms_ready.csv"

def clean_synsets(synsets_path, synsets_ready):
    """format and save synsets data so it can later be read by pd.read.csv()"""
    ar = []
    with open(synsets_path, 'r') as f:
        ar = f.readlines()
    ar = [line.strip().split(sep=',', maxsplit=2) for line in ar]
    data = pd.DataFrame(ar, columns = ['id', 'synset', 'definition'])
    data.tail()
    data.to_csv(synsets_ready, index=False)
    #pd.read_csv(synsets_ready, index_col=0).tail(5)
