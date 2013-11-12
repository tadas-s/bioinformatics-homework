from nose.tools import *
from bio import Genome
from mock import patch


def test_most_repeated_rough():
    #assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GCACACAGAC', 'GCGCACACAC']), Genome('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC').most_repeated_rough(10, 2))
    #assert_equal(set(['ccc', 'cct']), Genome('cccct').most_repeated_rough_top(3, 1))
    #assert_equal(set(['ccc', 'cct']), Genome('cccctggg').most_repeated_rough_top(3, 1))


#def test_zero_uses_simple_search():
#    with patch.object(Genome, 'most_repeated') as mock_method:
#        Genome('ctag').most_repeated_rough(3, 0)
#    mock_method.assert_called_once_with(3)


#@raises(ValueError)
#def test_raises_exception_with_large_values_of_d():
#    Genome('ctag').most_repeated_rough(3, 3)


#def test_empty():
#    assert_equal({}, Genome('').most_repeated_rough(3, 1))


#def test_too_small():
#    assert_equal({}, Genome('ctag').most_repeated_rough(5, 1))

