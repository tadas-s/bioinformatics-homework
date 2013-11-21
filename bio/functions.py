import bio
from bio.iterators import kmers


def peptide_encoded_by(dna, peptide):
    result = []
    for kmer in kmers(dna, len(peptide)*3):
        if bio.DNA(kmer).transcribes_to(peptide):
            result.append(kmer)

    return result
