#!/usr/bin/env python
import fileinput
import re
from bio import DNA


def main():
    input_file = fileinput.input()
    parameters = re.split("\s+", input_file.readline().strip())
    genome = DNA(parameters[0])
    print "\n".join(genome.most_repeated_rough(int(parameters[1]), int(parameters[2])))

if __name__ == '__main__':
    main()
