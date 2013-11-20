from nose.tools import *
from bio.generators import subpeptides


def test_cyclic_subpeptides():
    assert_equal(['L'], [pep for pep in subpeptides('L')])
    assert_equal(['L', 'E', 'LE', 'EL'], [pep for pep in subpeptides('LE')])
    assert_equal(['L', 'E', 'Q', 'LE', 'EQ', 'QL', 'LEQ', 'EQL', 'QLE'], [pep for pep in subpeptides('LEQ')])
