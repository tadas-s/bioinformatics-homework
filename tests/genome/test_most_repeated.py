from nose.tools import *
from bio import DNA


def test_empty():
    assert_equal({}, DNA('').most_repeated(1))


def test_too_small():
    assert_equal({}, DNA('ctag').most_repeated(5))


def test_nothing_to_do():
    assert_equal({'ctaag': 1}, DNA('ctaag').most_repeated(5))
    assert_equal({'c': 1}, DNA('c').most_repeated(1))

def test_basic():
    assert_equal({'c': 4, 't': 3, 'a': 2, 'g': 1}, DNA('cccctttaag').most_repeated(1))


def test_random_picks():
    assert_equal(3, DNA('cccttacc').most_repeated(2)['cc'])
    assert_equal(1, DNA('cccttacc').most_repeated(2)['tt'])
    assert_equal(1, DNA('cccttacc').most_repeated(2)['ta'])


def test_top_occurences():
    assert_equal(set([]), DNA('').most_repeated_top(2, 2))
    assert_equal(set(['cc', 'ct']), DNA('cccttaccct').most_repeated_top(2, 2))
