from nose.tools import *
from bio import Genome


def test_empty():
    assert_equal(set([]), Genome('').clumps(5, 100, 2))


def test_simple():
    assert_equal(set(['a']), Genome('a').clumps(1, 1, 1))
    assert_equal(set(['a', 'c', 't']), Genome('acttacttac').clumps(1, 1, 1))
    assert_equal(set(['tt', 'ac', 'ta', 'ct']), Genome('acttacttac').clumps(2, 6, 2))
    assert_equal(set(['tt', 'ac', 'ta', 'ct']), Genome('acttacttac').clumps(2, 10, 2))
    assert_equal(
        set(['cgaca', 'gaaga', 'aatgt']),
        Genome('cggactcgacagatgtgaagaaatgtgaagactgagtgaagagaagaggaaacacgacacgacattgcgacataatgtacgaatgtaatgtgcctatggc').clumps(5, 75, 4)
    )
    assert_equal(
        set(['cgaca', 'gaaga']),
        Genome('cggactcgacagatgtgaagaacgacaatgtgaagactcgacacgacagagtgaagagaagaggaaacattgtaa').clumps(5, 50, 4)
    )