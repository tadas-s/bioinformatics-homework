from nose.tools import *
from bio import DNA, Peptide


def test_transcribe():
    assert_equal('MA', DNA('ATGGCC').transcribe())
    assert_equal('GH', DNA('GGCCAT').transcribe())
    assert_equal('MA', DNA('ATGGCC').transcribe())


def test_transcribes_to():
    assert_true(DNA('ATGGCC').transcribes_to(Peptide('MA')))
    assert_true(DNA('GGCCAT').transcribes_to(Peptide('MA')))
    assert_true(DNA('ATGGCC').transcribes_to(Peptide('MA')))
