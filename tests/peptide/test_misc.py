from nose.tools import *
from bio import Peptide
from bio import RNA


def test_from_rna():
    assert_equal('MAMAPRTEINSTRING', Peptide.from_rna(RNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')))


def test_via_transcribe():
    assert_equal('MAMAPRTEINSTRING', RNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA').transcribe())


def test_integer_mass():
    assert_equal(113, Peptide('L').integer_mass())
    assert_equal(114, Peptide('N').integer_mass())
    assert_equal(227, Peptide('LN').integer_mass())
    assert_equal(484, Peptide('NQEL').integer_mass())
