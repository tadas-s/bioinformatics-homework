from nose.tools import *
from bio.modules import cyclopeptide_sequencing


def test_single_peptides():
    assert_equals(set(['T']), cyclopeptide_sequencing.single_peptides([101]))
    assert_equals(set([]), cyclopeptide_sequencing.single_peptides([200]))
    assert_equals(set(['T']), cyclopeptide_sequencing.single_peptides([101, 200]))


def test_spectrum_consistency():
    assert_equal(0, cyclopeptide_sequencing.spectrum_consistency(set([99, 101]), set([99, 101])))
    assert_equal(-1, cyclopeptide_sequencing.spectrum_consistency(set([99]), set([99, 101])))
    assert_equal(1, cyclopeptide_sequencing.spectrum_consistency(set([99, 101, 105]), set([99, 101])))
    assert_equal(1, cyclopeptide_sequencing.spectrum_consistency(set([99, 103]), set([99, 101])))
    assert_equal(1, cyclopeptide_sequencing.spectrum_consistency(set([131, 103]), set([99, 101])))


def test_do():
    assert_equals(set(['G']), cyclopeptide_sequencing.do(set([0, 57])))
    assert_equals(set(['GA', 'AG']), cyclopeptide_sequencing.do(set([0, 57, 71, 128])))
