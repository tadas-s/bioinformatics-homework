from nose.tools import *
from bio.lib import Genome


def test_empty():
    assert_true(Genome.is_similar('', '', 0))
    assert_true(Genome.is_similar('', '', 1))
    assert_true(Genome.is_similar('', '', 2))


def test_zero_distance():
    assert_true(Genome.is_similar('ctag', 'ctag', 0))
    assert_false(Genome.is_similar('ctag', 'gtag', 0))
    assert_false(Genome.is_similar('ctag', 'ctac', 0))
    #assert_false(Genome.is_similar('ctag', 'cctag', 0))
    #assert_false(Genome.is_similar('ctag', 'ctagc', 0))


def test_non_zero_distances():
    assert_true(Genome.is_similar('ctag', 'ctag', 1))
    assert_true(Genome.is_similar('ctag', 'gtag', 1))
    assert_true(Genome.is_similar('ctag', 'ctac', 1))
    #assert_true(Genome.is_similar('ctag', 'cctag', 1))
    #assert_true(Genome.is_similar('ctag', 'ctagc', 1))


def test_even_more_non_zero_distances():
    assert_true(Genome.is_similar('ctagg', 'ctacc', 2))
    assert_true(Genome.is_similar('ctagg', 'aaagg', 2))
    assert_false(Genome.is_similar('ctagg', 'ctccc', 2))
    assert_false(Genome.is_similar('cccgg', 'aaagg', 2))


def test_shifted():
    assert_true(Genome.is_similar('ctag', 'ccta', 1))
    assert_true(Genome.is_similar('ctag', 'tagc', 1))
    assert_false(Genome.is_similar('ctag', 'ccct', 1))
    assert_false(Genome.is_similar('ctag', 'agcc', 1))
