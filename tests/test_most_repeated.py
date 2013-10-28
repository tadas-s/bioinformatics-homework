from nose.tools import *
from bio.lib import Genome


def test_empty():
    assert_equal({}, Genome('').most_repeated(1))


def test_too_small():
    assert_equal({}, Genome('ctag').most_repeated(5))


def test_nothing_to_do():
    assert_equal({'ctaag': 1}, Genome('ctaag').most_repeated(5))
    assert_equal({'c': 1}, Genome('c').most_repeated(1))

def test_basic():
    assert_equal({'c': 4, 't': 3, 'a': 2, 'g': 1}, Genome('cccctttaag').most_repeated(1))


def test_random_picks():
    assert_equal(3, Genome('cccttacc').most_repeated(2)['cc'])
    assert_equal(1, Genome('cccttacc').most_repeated(2)['tt'])
    assert_equal(1, Genome('cccttacc').most_repeated(2)['ta'])


def test_top_occurences():
    assert_equal(set([]), Genome('').most_repeated_top(2, 2))
    assert_equal(set(['cc', 'ct']), Genome('cccttaccct').most_repeated_top(2, 2))
