from nose.tools import *
from bio.functions import peptide_encoded_by


def test_peptide_encoded_by():
    assert_equal(['ATGGCC', 'GGCCAT', 'ATGGCC'], peptide_encoded_by('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA', 'MA'))
