#!/usr/bin/env python
import fileinput
import re
from bio import DNA


def main():
    genome = DNA('')
    input_file = fileinput.input()
    for line in input_file:
        if 1 == (input_file.lineno() % 2):
            genome = DNA(line.strip())
        else:
            parameters = re.split("\s+", line.strip())
            print "\n".join(genome.clumps(int(parameters[0]), int(parameters[1]), int(parameters[2])))
            exit

if __name__ == '__main__':
    main()