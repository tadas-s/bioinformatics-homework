import re
from difflib import SequenceMatcher

class Genome(str):
    """ Silly genome class """

    def __new__(cls, content):
        instance = str.__new__(cls, re.sub('[^ctagCTAG]', '', content))
        return instance

    def most_repeated(self, k):
        """ Find most repeated k-mers in genome.
        Returns dict mapping of k-mer => repeats """
        result = {}
        for i in range(0, len(self) - k + 1):
            part = self[i:i+k]
            result[part] = result.setdefault(part, 0) + 1
        return result

    def most_repeated_top(self, k, quantity):
        """ Find number for top k-mers in genome
        Returns array of k-mers """
        mr = self.most_repeated(k)
        return set(sorted(mr, key=mr.get, reverse=True)[0:quantity])

    def reverse_complement(self):
        """ Get reverse complement of given genome """
        return ''.join(map(
            lambda s: {'a': 't', 'g': 'c', 'c': 'g', 't': 'a', 'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}[s],
            self[::-1])
        )

    def search(self, pattern):
        """ Get search of a pattern in the given genome
        Returns tuple of indexes"""
        return set(m.start() for m in re.finditer("(?=%s)" % pattern, self))

    def search_approximate(self, pattern, d):
        """
        @param pattern: str pattern to look for
        @param d: int of max allowed differences
        @return: set of integers
        """
        if d == 0:
            return self.search(pattern)

        if d >= len(pattern):
            raise ValueError("d-value of %s is too large for pattern '%s'" % (d, pattern))

        positions = set()

        for i in range(0, len(self) - len(pattern) + 1):
            matched = reduce(
                lambda x, y: (int(x[0] == x[1]) if type(x) is tuple else x) + (int(y[0] == y[1]) if type(y) is tuple else y),
                zip(pattern, self[i:i+len(pattern)])
            )
            if matched >= (len(pattern) - d):
                positions.add(i)

        return positions


    def clumps(self, k, region, times):
        """ Find k-sized patterns which form a clum (i.e. appear times or more) in region-sized region
        @rtype : set
        @param k: int
        @param region: int
        @param times: int
        """
        # Find most repeated items in the first window
        most_repeated = Genome(self[:region]).most_repeated(k)
        clumps = set()

        for pattern in most_repeated.iterkeys():
            if most_repeated[pattern] >= times:
                clumps.add(pattern)

        # Then slide the window and subtract one structure that went out of the window and add one that was introduced
        for i in range(1, len(self) - region):
            removed = self[i-1:i+k-1]
            introduced = self[i+region-k:i+region]
            most_repeated[removed] -= 1
            most_repeated[introduced] = most_repeated.setdefault(introduced, 0) + 1

            if most_repeated[introduced] >= times:
                clumps.add(introduced)

        return clumps

    def skew_values(self):
        """ Calculate skew values of the genome
        @return: tuple of integers
        """
        increments = {'c': -1, 'g': 1, 't': 0, 'a': 0}
        current = 0
        values = [current]

        for nucleotide in self:
            current += increments[nucleotide.lower()]
            values.append(current)

        return tuple(values)

    def skew_min(self):
        """ Locate skew minimums
        @return: tuple of integers
        """
        values = self.skew_values()
        minimum = min(values)
        return tuple(filter(lambda i: values[i] == minimum, range(0, len(values))))
