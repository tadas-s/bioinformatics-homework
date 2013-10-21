from nose.tools import *
from bio.lib import most_repeated, most_repeated_top


def test_empty():
    assert_equal({}, most_repeated(1, ''))


def test_too_small():
    assert_equal({}, most_repeated(5, 'abcd'))


def test_nothing_to_do():
    assert_equal({'abcde': 1}, most_repeated(5, 'abcde'))


def test_basic():
    assert_equal({'a': 3, 'b': 2, 'c': 1}, most_repeated(1, 'aaabbc'))


def test_random_picks():
    assert_equal(3, most_repeated(2, 'aaabbcaa')['aa'])
    assert_equal(1, most_repeated(2, 'aaabbcaa')['bb'])
    assert_equal(1, most_repeated(2, 'aaabbcaa')['bc'])

def test_top_occurences():
    assert_equal([], most_repeated_top(2, 2, ''))
    assert_equal(['aa', 'ab'], most_repeated_top(2, 2, 'aaabbcaaab'))
