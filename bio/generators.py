from itertools import product
import bio

def kmer_probability_generator(probabilities):
    sorted_nucleotides = []

    for p in probabilities:
        sorted_nucleotides.append(sorted(p.iterkeys(), key=lambda k: p[k], reverse=True))

    for sequence in product(*sorted_nucleotides):
        yield ''.join(sequence)


def kmer_probability_generator(probabilities):
    sorted_nucleotides = []
    indexes = []
    k = len(probabilities)

    for p in probabilities:
        sorted_nucleotides.append(sorted(p.iterkeys(), key=lambda k: p[k], reverse=True))
        indexes.append(range(4))

    for range_sum in range(k*4):
        for sequence in product(*indexes):
            if sum(sequence) == range_sum:
                yield ''.join(map(lambda (index, nucleotide_index): sorted_nucleotides[index][nucleotide_index], enumerate(sequence)))


def kmer_probability_generator_alternative_needs_work(probabilities):
    sorted_nucleotides = []
    offsets = []

    for p in probabilities:
        sorted_nucleotides.append(sorted(p.iterkeys(), key=lambda k: p[k], reverse=True))
        offsets.append(0)

    while True:

        yield ''.join(sorted_nucleotides[index][offset] for index, offset in enumerate(offsets))

        min_diff = 1.0
        offset_index = None

        for index, p in enumerate(sorted_nucleotides):
            if offsets[index] < 3:
                this_diff = probabilities[index][p[offsets[index]]] - probabilities[index][p[offsets[index] + 1]]
                if this_diff < min_diff:
                    min_diff = this_diff
                    offset_index = index

        if offset_index is not None:
            offsets[offset_index] += 1
        else:
            break


def subpeptides(peptide):
    closed = peptide + peptide

    for length in range(1, len(peptide)+1):
        visited = set([])
        for start in range(len(peptide)):
            pep = closed[start:start+length]
            if pep not in visited:
                yield pep
            visited.add(pep)


def cyclospectrum(peptide):
    closed = peptide + peptide

    # for some reason.. it's always in result
    yield 0

    for length in range(1, len(peptide)):
        for start in range(len(peptide)):
            yield bio.Peptide(closed[start:start+length]).integer_mass()

    # edge case - while all others have
    yield bio.Peptide(peptide).integer_mass()
