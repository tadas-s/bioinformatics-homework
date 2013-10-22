from nose.tools import *
from bio.lib import Genome


def test_empty():
    assert_equal((), Genome('').positions('a'))


def test_single_letters():
    assert_equal((0, 1, 2), Genome('aaa').positions('a'))


def test_multiple_letters():
    assert_equal((0, 3), Genome('ctactaccc').positions('cta'))


def test_multiple_overlapping():
    assert_equal((0, 2, 4), Genome('cacacac').positions('cac'))