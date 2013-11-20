from nose.tools import *
from bio.peptide import Translator

test_table = {
    'AAA': 'K',
    'AAG': 'K',
    'ACA': 'T',
    'ACC': 'T',
    'CUC': 'L',
    'CUG': 'L'
}


def test_init():
    Translator.rna_to_peptide(table=test_table)
    assert_equal(test_table, Translator.rna_to_peptide())


def test_init():
    Translator.rna_to_peptide(table=test_table)
    assert_equal({'AAA': 'K', 'AAG': 'K',  'ACA': 'T', 'ACC': 'T', 'CTC': 'L', 'CTG': 'L'}, Translator.dna_to_peptide())

