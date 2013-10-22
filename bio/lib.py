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
        return tuple(sorted(mr, key=mr.get, reverse=True)[0:quantity])

    def reverse_complement(self):
        """ Get reverse complement of given genome """
        return ''.join(map(
            lambda s: {'a': 't', 'g': 'c', 'c': 'g', 't': 'a', 'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}[s],
            self[::-1])
        )

    def positions(self, pattern):
        """ Get positions of a pattern in the given genome
        Returns tuple of indexes"""
        pass
