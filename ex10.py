#!/usr/bin/env python
import fileinput
from bio.generators import cyclospectrum


def main():
    input_file = fileinput.input()
    peptide = input_file.readline().strip()
    print " ".join([str(mass_str) for mass_str in sorted([mass for mass in cyclospectrum(peptide)])])

if __name__ == '__main__':
    main()