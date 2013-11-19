from nose.tools import *
from bio import Genome


def test_empty():
    assert_equal('', Genome('').reverse_complement())


def test_single():
    assert_equal('a', Genome('t').reverse_complement())
    assert_equal('g', Genome('c').reverse_complement())
    assert_equal('c', Genome('g').reverse_complement())
    assert_equal('t', Genome('a').reverse_complement())
    assert_equal('A', Genome('T').reverse_complement())
    assert_equal('G', Genome('C').reverse_complement())
    assert_equal('C', Genome('G').reverse_complement())
    assert_equal('T', Genome('A').reverse_complement())


def test_many():
    assert_equal('ACCGGGTTTT', Genome('AAAACCCGGT').reverse_complement())
    assert_equal('AAAACCCGGT', Genome('ACCGGGTTTT').reverse_complement())
