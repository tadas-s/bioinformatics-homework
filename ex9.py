#!/usr/bin/env python
import fileinput
from bio.functions import peptide_encoded_by


def main():
    input_file = fileinput.input()
    dna = input_file.readline().strip()
    peptide = input_file.readline().strip()
    print "\n".join(peptide_encoded_by(dna, peptide))

if __name__ == '__main__':
    main()