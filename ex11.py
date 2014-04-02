#!/usr/bin/env python
import fileinput
from bio.modules import cyclopeptide_sequencing


def main():
    input_file = fileinput.input()
    spectrum = set(map(lambda mass: int(mass), input_file.readline().strip().split(' ')))
    print spectrum
    matches = cyclopeptide_sequencing.as_masses(spectrum)
    print matches
    print "\n".join(map(lambda masses: '-'.join(map(str, masses)), matches))

if __name__ == '__main__':
    main()