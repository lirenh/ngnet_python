import pytest
from ..ngnet.wordnet import *
from ..config import *

def test_hypnoyms():
    wn1 = WordNet(TEST_SYNSETS1, TEST_HYPONYMS1)
    assert wn1.hypnoyms('jump') == {'jump', 'saltation', 'leap'}
    assert wn1.nouns() == {'alteration', 'natural_event', 'human_action', 'change', 'demotion', 'conversion', 'happening', 'occurrence', 'act', 'increase', 'event', 'adjustment', 'transition', 'leap', 'saltation', 'variation', 'occurrent', 'action', 'modification', 'jump', 'human_activity', 'mutation'}

    wn2 = WordNet(TEST_SYNSETS2, TEST_HYPONYMS2)
    assert wn2.hypnoyms('haemoglobin') == {'oxyhaemoglobin', 'hemoglobin', 'haemoglobin', 'oxyhemoglobin', 'Hb'}
