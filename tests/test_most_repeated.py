from nose.tools import *
from bio.lib import Genome


def test_empty():
    assert_equal({}, Genome('').most_repeated(1))


def test_too_small():
    assert_equal({}, Genome('abcd').most_repeated(5))


def test_nothing_to_do():
    assert_equal({'abcde': 1}, Genome('abcde').most_repeated(5))
    assert_equal({'a': 1}, Genome('a').most_repeated(1))

def test_basic():
    assert_equal({'a': 3, 'b': 2, 'c': 1}, Genome('aaabbc').most_repeated(1))


def test_random_picks():
    assert_equal(3, Genome('aaabbcaa').most_repeated(2)['aa'])
    assert_equal(1, Genome('aaabbcaa').most_repeated(2)['bb'])
    assert_equal(1, Genome('aaabbcaa').most_repeated(2)['bc'])


def test_top_occurences():
    assert_equal(set([]), Genome('').most_repeated_top(2, 2))
    assert_equal(set(['aa', 'ab']), Genome('aaabbcaaab').most_repeated_top(2, 2))
