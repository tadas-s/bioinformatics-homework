from nose.tools import *
from bio import Peptide
from bio import RNA


def test_from_rna():
    assert_equal('MAMAPRTEINSTRING', Peptide.from_rna(RNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')))


def test_via_transcribe():
    assert_equal('MAMAPRTEINSTRING', RNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA').transcribe())
