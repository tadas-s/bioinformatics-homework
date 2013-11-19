from nose.tools import *
from bio import Genome


def test_empty():
    assert_equals((0,), Genome('').skew_values())


def test_minimal_simple():
    assert_equals((0, 0), Genome('a').skew_values())
    assert_equals((0, 0), Genome('t').skew_values())
    assert_equals((0, -1), Genome('c').skew_values())
    assert_equals((0, 1), Genome('g').skew_values())


def test_multiple():
    assert_equal(
        (0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2),
        Genome('CATGGGCATCGGCCATACGCC').skew_values()
    )


def test_skew_min():
    assert_equal((11, 24), Genome('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT').skew_min())
