from nose.tools import *
from bio import Genome


def test_constructor_strips_whitespace():
    assert_equal('CTAG', Genome(' CTAG '))
    assert_equal('ctag', Genome("\tctag\t"))
    assert_equal('CTAG', Genome("\nCTAG\n"))
    assert_equal('ctag', Genome("\rctag\r"))


@raises(ValueError)
def test_kmers_of_zero():
    Genome('').kmers_of(0)


@raises(ValueError)
def test_kmers_of_minus_one():
    Genome('').kmers_of(-1)


def test_kmers_of():
    assert_equal(0, Genome('').kmers_of(1))
    assert_equal(0, Genome('').kmers_of(2))
    assert_equal(1, Genome('c').kmers_of(1))
    assert_equal(2, Genome('cc').kmers_of(1))
    assert_equal(2, Genome('cta').kmers_of(2))
    assert_equal(1, Genome('cta').kmers_of(3))
    assert_equal(27, Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').kmers_of(4))
