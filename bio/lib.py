import re

class Genome(str):
    """ Silly genome class """

    def most_repeated(self, k):
        """ Find most repeated k-mers in genome.
        Returns dict mapping of k-mer => repeats """
        result = {}
        for i in range(0, len(self) - k + 1):
            part = self[i:i+k]
            if part in result:
                result[part] += 1
            else:
                result[part] = 1
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

    def positions(self, pattern):
        """ Get positions of a pattern in the given genome
        Returns tuple of indexes"""
        return set(m.start() for m in re.finditer("(?=%s)" % pattern, self))

    def clumps(self, k, region, times):
        """ Find k-sized patterns which form a clum (i.e. appear times or more) in region-sized region """
        clumps = []
        for i in range(0, len(self) - region + 1):
            mr = Genome(self[i:i+region]).most_repeated(k)
            clumps += filter(lambda key: mr[key] >= times, mr.keys())
        return set(clumps)
