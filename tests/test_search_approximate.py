from nose.tools import *
from bio.lib import Genome
from mock import patch


def test_empty():
    assert_equal(set(), Genome('').search_approximate('ctag', 1))


def test_zero_uses_simple_search():
    with patch.object(Genome, 'search') as mock_method:
        Genome('ctag').search_approximate('ctag', 0)
    mock_method.assert_called_once_with('ctag')


@raises(ValueError)
def test_raises_exception_with_large_values_of_d():
    Genome('ctag').search_approximate('cta', 4)


def test_single_letters():
    assert_equal(set([0]), Genome('ctat').search_approximate('ctag', 1))
    assert_equal(set([4]), Genome('ttttctat').search_approximate('ctag', 1))
    assert_equal(set([0]), Genome('ctagtttt').search_approximate('ctag', 1))


def test_non_trivial():
    assert_equal(
        set([6, 7, 26, 27]),
        Genome('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT').search_approximate('ATTCTGGA', 3)
    )

#def test_multiple_letters():
#    assert_equal(set([0, 3]), Genome('ctactaccc').search('cta'))


#def test_multiple_overlapping():
#    assert_equal(set([0, 2, 4]), Genome('cacacac').search('cac'))