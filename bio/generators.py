from itertools import product


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
