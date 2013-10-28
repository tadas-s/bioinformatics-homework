#!/usr/bin/env python
import fileinput
from bio.lib import Genome


def main():
    input_file = fileinput.input()
    pattern = input_file.readline().strip()
    genome = Genome(input_file.readline())
    d = int(input_file.readline().strip())
    print(' '.join([str(x) for x in genome.search_approximate(pattern, d)]))

if __name__ == '__main__':
    main()