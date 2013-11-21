from nose.tools import *
from bio import DNA


def test_empty():
    assert_equal(set([]), DNA('').clumps(5, 100, 2))


def test_simple():
    assert_equal(set(['a']), DNA('a').clumps(1, 1, 1))
    assert_equal(set(['a', 'c', 't']), DNA('acttacttac').clumps(1, 1, 1))
    assert_equal(set(['tt', 'ac', 'ta', 'ct']), DNA('acttacttac').clumps(2, 6, 2))
    assert_equal(set(['tt', 'ac', 'ta', 'ct']), DNA('acttacttac').clumps(2, 10, 2))
    assert_equal(
        set(['cgaca', 'gaaga', 'aatgt']),
        DNA('cggactcgacagatgtgaagaaatgtgaagactgagtgaagagaagaggaaacacgacacgacattgcgacataatgtacgaatgtaatgtgcctatggc').clumps(5, 75, 4)
    )
    assert_equal(
        set(['cgaca', 'gaaga']),
        DNA('cggactcgacagatgtgaagaacgacaatgtgaagactcgacacgacagagtgaagagaagaggaaacattgtaa').clumps(5, 50, 4)
    )