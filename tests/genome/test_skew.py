from nose.tools import *
from bio import DNA


def test_empty():
    assert_equals((0,), DNA('').skew_values())


def test_minimal_simple():
    assert_equals((0, 0), DNA('a').skew_values())
    assert_equals((0, 0), DNA('t').skew_values())
    assert_equals((0, -1), DNA('c').skew_values())
    assert_equals((0, 1), DNA('g').skew_values())


def test_multiple():
    assert_equal(
        (0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2),
        DNA('CATGGGCATCGGCCATACGCC').skew_values()
    )


def test_skew_min():
    assert_equal((11, 24), DNA('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT').skew_min())
