import glob
import pandas as pd
from config import *

def get_nouns():
    """
    Get all the nouns and save them to NGRAMS_NOUN_PATH
    """
    for f in glob.glob(NGRAMS_PATH + '*'):
        output = f.split('/')[-1].replace('all', 'noun') + ".csv"
        data = pd.read_csv(f, header=None, names=['word','year','count','sources'], delim_whitespace=True)
        criterion = data['word'].map(lambda x: str(x).endswith('_NOUN'))
        new = data[criterion]
        new['word'] = new['word'].map(lambda x: x[:-5])
        new.to_csv(NGRAMS_NOUN_PATH + output, index=False)

def get_lower_alpha():
    """
    Get nouns which are all-lowercase ang all-alphabetic, and save them to NGRAMS_LOWER_ALPHA_PATH
    """
    lst = []
    for f in glob.glob(NGRAMS_NOUN_PATH + '*'):
        lan_file = f.split('/')[-1].replace('noun', 'lower-alpha-noun')
        data = pd.read_csv(f)
        criterion_lower_alpha = data['word'].map(lambda x: str(x).isalpha() and str(x).islower())
        alpha_nouns = data[criterion_lower_alpha]
        lst.append(alpha_nouns)
        alpha_nouns.to_csv(NGRAMS_LOWER_ALPHA_PATH + lan_file, index=False)
    all = pd.concat(lst)
    all.to_csv(NGRAMS_LOWER_ALPHA_PATH + "googlebooks-eng-lower-alpha-noun-1gram-20120701-all.csv")
