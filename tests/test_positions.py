from nose.tools import *
from bio.lib import positions


def test_empty():
    assert_equal((), most_repeated(1, ''))
