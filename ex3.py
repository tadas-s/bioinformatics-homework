#!/usr/bin/env python
import sys
import fileinput
from bio.lib import Genome


def main(argv):
    for line in fileinput.input(argv[1]):
        print "\n".join(map(lambda e: str(e), Genome(line.strip()).positions(argv[0])))

if __name__ == '__main__':
    main(sys.argv[1:])