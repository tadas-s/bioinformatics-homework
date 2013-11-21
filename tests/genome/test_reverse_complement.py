from nose.tools import *
from bio import DNA


def test_empty():
    assert_equal('', DNA('').reverse_complement())


def test_single():
    assert_equal('a', DNA('t').reverse_complement())
    assert_equal('g', DNA('c').reverse_complement())
    assert_equal('c', DNA('g').reverse_complement())
    assert_equal('t', DNA('a').reverse_complement())
    assert_equal('A', DNA('T').reverse_complement())
    assert_equal('G', DNA('C').reverse_complement())
    assert_equal('C', DNA('G').reverse_complement())
    assert_equal('T', DNA('A').reverse_complement())


def test_many():
    assert_equal('ACCGGGTTTT', DNA('AAAACCCGGT').reverse_complement())
    assert_equal('AAAACCCGGT', DNA('ACCGGGTTTT').reverse_complement())
