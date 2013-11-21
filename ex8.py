#!/usr/bin/env python
import fileinput
import re
from bio import DNA


def main():
    input_file = fileinput.input()
    genome = DNA(input_file.readline().strip())
    parameters = re.split("\s+", input_file.readline().strip())
    print "\n".join(genome.most_repeated_rough_with_reverse_complements(int(parameters[0]), int(parameters[1])))

if __name__ == '__main__':
    main()
