from nose.tools import *
from bio import Genome
from mock import patch


def test_most_repeated_rough():
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    assert_equal(set(['GATG', 'ATGC', 'ATGT']), Genome('ACGTTGCATGTCGCATGATGCATGAGAGCT').most_repeated_rough(4, 1))
    #assert_equal(set(['GCACACAGAC', 'GCGCACACAC']), Genome('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC').most_repeated_rough(10, 2))
