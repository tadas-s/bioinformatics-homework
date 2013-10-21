#!/usr/bin/env python
import sys
import fileinput
from bio.lib import reverse_complement


def main(argv):
    for line in fileinput.input():
        print reverse_complement(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])