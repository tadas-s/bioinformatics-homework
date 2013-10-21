#!/usr/bin/env python
import sys
import fileinput
from ex1.lib import most_repeated_top


def main(argv):
    for line in fileinput.input(argv[2]):
        print most_repeated_top(int(argv[0]), int(argv[1]), line)


if __name__ == '__main__':
    main(sys.argv[1:])