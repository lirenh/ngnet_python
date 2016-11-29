import numpy as np
import pandas as pd

S_TESTPATH1="../test_data/wordnet/synsets14.txt"
S_TESTPATH2="../test_data/wordnet/synsets1000-subgraph.txt"
HPATH="../test-data/wordnet/hyponyms1000-subgraph.txt"

def clean_synsets(synsets_path):
    """format and save synsets data so it can later be read by pd.read.csv()"""
    ar = []
    with open(synsets_path, 'r') as f:
        ar = f.readlines()
    ar = [line.strip().split(sep=',', maxsplit=2) for line in ar]
    data = pd.DataFrame(ar, columns = ['id', 'synset', 'definition'])
    data.tail()
    synsets_clean = synsets_path.replace(".txt", "_clean.csv")
    data.to_csv(synsets_clean, index=False)
    #pd.read_csv(synsets_ready, index_col=0).tail(5)
