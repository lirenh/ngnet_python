import pytest
from ..ngnet.digraph import *

g1 = Digraph(14)
g1.add_edge(0, 1);
g1.add_edge(1, 2);
g1.add_edge(2, 13);
g1.add_edge(3, 4);
g1.add_edge(5, 6);
g1.add_edge(5, 7);
g1.add_edge(6, 11);
g1.add_edge(7, 12);
g1.add_edge(7, 13);
g1.add_edge(6, 13);
g1.add_edge(8, 10);
g1.add_edge(9, 10);

def test_digraph():
    assert g1.V == 14
    assert g1.E == 12
    assert g1.adj(5) == [6,7]

def test_descendants():
    assert descendants(g1, (5,)) == [5, 6, 7, 11, 12, 13]
    assert descendants(g1, (0, 1)) == [0, 1, 2, 13]
