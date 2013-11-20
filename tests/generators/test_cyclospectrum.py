from nose.tools import *
from bio.generators import cyclospectrum


def test_cyclospectrum():
    assert_equal([0, 113], [mass for mass in cyclospectrum('L')])
    assert_equal(sorted([0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]), sorted([mass for mass in cyclospectrum('LEQN')]))
