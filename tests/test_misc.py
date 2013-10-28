from nose.tools import *
from bio.lib import Genome


def test_constructor_strips_whitespace():
    assert_equal('CTAG', Genome(' CTAG '))
    assert_equal('ctag', Genome("\tctag\t"))
    assert_equal('CTAG', Genome("\nCTAG\n"))
    assert_equal('ctag', Genome("\rctag\r"))
