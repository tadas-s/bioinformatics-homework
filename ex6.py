#!/usr/bin/env python
import fileinput
from bio import DNA


def main():
    input_file = fileinput.input()
    pattern = input_file.readline().strip()
    genome = DNA(input_file.readline())
    d = int(input_file.readline().strip())
    print(' '.join([str(x) for x in genome.search_rough(pattern, d)]))

if __name__ == '__main__':
    main()
