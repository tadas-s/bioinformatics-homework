from nose.tools import *
from bio import Genome, Peptide


def test_transcribe():
    assert_equal('MA', Genome('ATGGCC').transcribe())
    assert_equal('GH', Genome('GGCCAT').transcribe())
    assert_equal('MA', Genome('ATGGCC').transcribe())


def test_transcribes_to():
    assert_true(Genome('ATGGCC').transcribes_to(Peptide('MA')))
    assert_true(Genome('GGCCAT').transcribes_to(Peptide('MA')))
    assert_true(Genome('ATGGCC').transcribes_to(Peptide('MA')))
