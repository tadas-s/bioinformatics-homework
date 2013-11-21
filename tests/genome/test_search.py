from nose.tools import *
from bio import DNA


def test_empty():
    assert_equal(set([]), DNA('').search('a'))


def test_single_letters():
    assert_equal(set([0, 1, 2]), DNA('aaa').search('a'))


def test_multiple_letters():
    assert_equal(set([0, 3]), DNA('ctactaccc').search('cta'))


def test_multiple_overlapping():
    assert_equal(set([0, 2, 4]), DNA('cacacac').search('cac'))