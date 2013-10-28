#!/usr/bin/env python
import fileinput
from bio.lib import Genome


def main():
    for line in fileinput.input():
        print(' '.join([str(x) for x in Genome(line).skew_values()]))

if __name__ == '__main__':
    main()
