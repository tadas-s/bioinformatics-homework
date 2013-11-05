from nose.tools import *
from bio.lib import Genome
from mock import patch


def test_zero_uses_simple_search():
    with patch.object(Genome, 'most_repeated') as mock_method:
        Genome('ctag').most_repeated_rough(3, 0)
    mock_method.assert_called_once_with(3)


@raises(ValueError)
def test_raises_exception_with_large_values_of_d():
    Genome('ctag').most_repeated_rough(3, 3)


def test_empty():
    assert_equal({}, Genome('').most_repeated_rough(3, 1))


def test_too_small():
    assert_equal({}, Genome('ctag').most_repeated_rough(5, 1))


def test_nothing_to_do():
    assert_equal({'ctaag': {'count': 1, 'similar': set()}}, Genome('ctaag').most_repeated_rough(5, 1))
    assert_equal({'cc': {'count': 1, 'similar': set()}}, Genome('cc').most_repeated_rough(2, 1))


def test_simple_cases():
    assert_equal(2, Genome('cccct').most_repeated_rough(3, 1)['ccc']['count'])
    assert_equal(1, Genome('cccct').most_repeated_rough(3, 1)['cct']['count'])
    assert_equal(2, Genome('cactttcactttcatccctac').most_repeated_rough(3, 1)['cac']['count'])


def test_most_repeated_rough_top():
    #assert_equal(set(['ccc', 'cct']), Genome('cccct').most_repeated_rough_top(3, 1))
    #assert_equal(set(['ccc', 'cct']), Genome('cccctggg').most_repeated_rough_top(3, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough_top(4, 1))
