import pytest
from ..wordnet.wordnet import *

SPATH1="/home/liren/stash/ngnet/test_data/wordnet/synsets1000-subgraph.txt"
HPATH1="/home/liren/stash/ngnet/test_data/wordnet/hyponyms1000-subgraph.txt"
SPATH2="/home/liren/stash/ngnet/test_data/wordnet/synsets14.txt"
HPATH2="/home/liren/stash/ngnet/test_data/wordnet/hyponyms14.txt"

def test_hypnoyms():
    wn1 = WordNet(SPATH1, HPATH1)
    assert wn1.hypnoyms('haemoglobin') == {'oxyhaemoglobin', 'hemoglobin', 'haemoglobin', 'oxyhemoglobin', 'Hb'}

    wn2 = WordNet(SPATH2, HPATH2)
    assert wn2.hypnoyms('jump') == {'jump', 'saltation', 'leap'}
    assert wn2.nouns() == {'alteration', 'natural_event', 'human_action', 'change', 'demotion', 'conversion', 'happening', 'occurrence', 'act', 'increase', 'event', 'adjustment', 'transition', 'leap', 'saltation', 'variation', 'occurrent', 'action', 'modification', 'jump', 'human_activity', 'mutation'}
