from nose.tools import *
from bio import DNA


def test_constructor_strips_whitespace():
    assert_equal('CTAG', DNA(' CTAG '))
    assert_equal('ctag', DNA("\tctag\t"))
    assert_equal('CTAG', DNA("\nCTAG\n"))
    assert_equal('ctag', DNA("\rctag\r"))


@raises(ValueError)
def test_kmers_of_zero():
    DNA('').kmers_of(0)


@raises(ValueError)
def test_kmers_of_minus_one():
    DNA('').kmers_of(-1)


def test_kmers_of():
    assert_equal(0, DNA('').kmers_of(1))
    assert_equal(0, DNA('').kmers_of(2))
    assert_equal(1, DNA('c').kmers_of(1))
    assert_equal(2, DNA('cc').kmers_of(1))
    assert_equal(2, DNA('cta').kmers_of(2))
    assert_equal(1, DNA('cta').kmers_of(3))
    assert_equal(27, DNA('ACGTTGCATGTCGCATGATGCATGAGAGCT').kmers_of(4))
