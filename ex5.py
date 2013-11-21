#!/usr/bin/env python
import fileinput
from bio import DNA


def main():
    for line in fileinput.input():
        print(' '.join([str(x) for x in DNA(line).skew_min()]))

if __name__ == '__main__':
    main()
