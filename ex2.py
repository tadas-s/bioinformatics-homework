#!/usr/bin/env python
import sys
import fileinput
from bio.lib import Genome


def main(argv):
    for line in fileinput.input():
        print Genome(line.strip()).reverse_complement()


if __name__ == '__main__':
    main(sys.argv[1:])