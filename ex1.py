#!/usr/bin/env python
import sys
import fileinput
from bio import DNA

def main(argv):
    for line in fileinput.input(argv[2]):
        print DNA(line).most_repeated_top(int(argv[0]), int(argv[1]))


if __name__ == '__main__':
    main(sys.argv[1:])