from nose.tools import *
from bio import DNA
from mock import patch


def test_most_repeated_rough():
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), DNA('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    #assert_equal(set(['GCACACAGAC', 'GCGCACACAC']), DNA('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC').most_repeated_rough(10, 2))

def test_most_repeated_rough_with_reverse_complements():
    assert_equal(set(['ATGT', 'ACAT']), DNA('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough_with_reverse_complements(4, 1))
