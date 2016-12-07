import pytest
from ..config import *
from ..wordnet.ngram import *

def test_g():
    g = NGram(TEST_WORDS, TOTAL_COUNT)
    assert g.count_in('qib', 2002) == 5
    assert g.word_history('qinggui', 2007,2008)['count'].sum() == 142
    assert g.hist_sum(['qib', 'qinggui'], 2004, 2005)['count'].sum() == 257
    assert g.word_rank(2008).at[1,'count'] == 113
    assert g.word_rank(2008).at[3,'count'] == 1
