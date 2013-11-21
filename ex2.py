#!/usr/bin/env python
import sys
import fileinput
from bio import DNA


def main(argv):
    for line in fileinput.input():
        print DNA(line.strip()).reverse_complement()


if __name__ == '__main__':
    main(sys.argv[1:])