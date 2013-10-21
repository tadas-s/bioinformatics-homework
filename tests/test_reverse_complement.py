from nose.tools import *
from bio.lib import reverse_complement


def test_empty():
    assert_equal('', reverse_complement(''))

def test_single():
    assert_equal('a', reverse_complement('t'))
    assert_equal('g', reverse_complement('c'))
    assert_equal('c', reverse_complement('g'))
    assert_equal('t', reverse_complement('a'))
    assert_equal('A', reverse_complement('T'))
    assert_equal('G', reverse_complement('C'))
    assert_equal('C', reverse_complement('G'))
    assert_equal('T', reverse_complement('A'))

def test_many():
    assert_equal('ACCGGGTTTT', reverse_complement('AAAACCCGGT'))
    assert_equal('AAAACCCGGT', reverse_complement('ACCGGGTTTT'))
