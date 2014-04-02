from bio.generators import cyclospectrum
from bio.peptide import peptide_integer_masses


def do(spectrum):
    """
    @param spectrum: set
    @param candidate: str - do not set, used for recursion
    @return: set
    """
    sps = single_peptides(spectrum)

    def do_recursive(candidate):

        matches = set([])

        for peptide in sps:
            extended_candidate = candidate + peptide
            extended_candidate_spectrum = set([mass for mass in cyclospectrum(extended_candidate)])

            if spectrum_consistency(extended_candidate_spectrum, spectrum) == 0:
                matches.add(extended_candidate)
            elif spectrum_consistency(extended_candidate_spectrum, spectrum) == -1:
                matches = matches.union(do_recursive(extended_candidate))
            # else inconsistent and therefore nothing to do

        return matches

    return do_recursive('')


def as_masses(spectrum):
    peps = do(spectrum)
    masses = []

    for pep in peps:
        pep_masses = map(lambda p: peptide_integer_masses[p], pep)
        masses.append(pep_masses)

    return masses


def single_peptides(from_spectrum):
    masses = set(peptide_integer_masses.values()).intersection(set(from_spectrum))
    peptides = set(map(lambda mass: peptide_integer_masses.keys()[peptide_integer_masses.values().index(mass)], masses))
    return peptides

def spectrum_consistency(spectrum_a, spectrum_b):
    """
    @param spectrum_a: set
    @param spectrum_b: set
    @return: int
    """
    if spectrum_a == spectrum_b:
        return 0
    elif len(spectrum_a.intersection(spectrum_b)) == len(spectrum_a):
        return -1
    elif len(spectrum_a.intersection(spectrum_b)) < len(spectrum_a):
        return 1
