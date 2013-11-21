#!/usr/bin/env python
import sys
import fileinput
from bio import DNA


def main(argv):
    for line in fileinput.input(argv[1]):
        print "\n".join(map(lambda e: str(e), DNA(line.strip()).search(argv[0])))

if __name__ == '__main__':
    main(sys.argv[1:])