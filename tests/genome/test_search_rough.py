from nose.tools import *
from bio import DNA
from mock import patch


def test_empty():
    assert_equal(set(), DNA('').search_rough('ctag', 1))


def test_zero_uses_simple_search():
    with patch.object(DNA, 'search') as mock_method:
        DNA('ctag').search_rough('ctag', 0)
    mock_method.assert_called_once_with('ctag')


@raises(ValueError)
def test_raises_exception_with_large_values_of_d():
    DNA('ctag').search_rough('cta', 4)


def test_single_letters():
    assert_equal(set([0]), DNA('ctat').search_rough('ctag', 1))
    assert_equal(set([4]), DNA('ttttctat').search_rough('ctag', 1))
    assert_equal(set([0]), DNA('ctagtttt').search_rough('ctag', 1))


def test_non_trivial():
    assert_equal(
        set([6, 7, 26, 27]),
        DNA('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT').search_rough('ATTCTGGA', 3)
    )

#def test_multiple_letters():
#    assert_equal(set([0, 3]), DNA('ctactaccc').search('cta'))


#def test_multiple_overlapping():
#    assert_equal(set([0, 2, 4]), DNA('cacacac').search('cac'))