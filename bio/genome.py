import re
from bio.generators import kmer_probability_generator
import bio

class Genome(str):
    """ Silly genome class """

    def __new__(cls, content):
        instance = str.__new__(cls, re.sub('[^ctagCTAG]', '', content))
        return instance

    def kmers_of(self, k):
        """ Quantity of k-mers in genome
        @param k: int
        @return: int
        """
        if k < 1:
            raise ValueError("There is no such thing as %s-mer" % (k,))

        return max(0, len(self) - k + 1)

    def most_repeated(self, k):
        """ Find most repeated k-mers in genome.
        Returns dict mapping of k-mer => repeats """
        result = {}
        for i in range(0, len(self) - k + 1):
            part = self[i:i + k]
            result[part] = result.setdefault(part, 0) + 1
        return result

    def most_repeated_rough(self, k, d):
        # Take most frequent kmers ....
        mr = self.most_repeated(k)
        must_match = k - d

        top_count = -1
        top_set = set([])

        for candidate in kmer_probability_generator(self.kmer_nucleotide_probabilities(k)):
            candidate = candidate.upper()
            current_count = 0

            for kmer, count in mr.iteritems():
                matched = sum(candidate[index] == kmer[index] for index in range(k))
                if matched >= must_match:
                    current_count += count

            if current_count > top_count:
                top_count = current_count
                top_set = set([candidate.upper()])
                print "top: %s, set:\n%s" % (top_count, "\n".join(top_set))
            elif current_count == top_count:
                top_set.add(candidate.upper())
                print "top: %s, set:\n%s" % (top_count, "\n".join(top_set))

        return top_set

    def most_repeated_rough_with_reverse_complements(self, k, d):
        # Take most frequent kmers ....
        mr = self.most_repeated(k)
        must_match = k - d

        top_count = -1
        top_set = set([])

        for candidate in kmer_probability_generator(self.kmer_nucleotide_probabilities(k)):
            candidate = candidate.upper()
            candidate_revc = Genome(candidate).reverse_complement()
            current_count = 0

            for kmer, count in mr.iteritems():
                matched = sum(candidate[index] == kmer[index] for index in range(k))
                if matched >= must_match:
                    current_count += count
                matched = sum(candidate_revc[index] == kmer[index] for index in range(k))
                if matched >= must_match:
                    current_count += count

            if current_count > top_count:
                top_count = current_count
                top_set = set([candidate, candidate_revc])
                print "top: %s, set:\n%s" % (top_count, "\n".join(top_set))
            elif current_count == top_count:
                top_set.add(candidate)
                top_set.add(candidate_revc)
                print "top: %s, set:\n%s" % (top_count, "\n".join(top_set))

        return top_set

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

    def search_rough(self, pattern, d):
        """
        @param pattern: str pattern to look for
        @param d: int of max allowed differences
        @return: set of integers
        """
        if 0 == d:
            return self.search(pattern)

        if len(pattern) <= d:
            raise ValueError("d-value of %s is too large for pattern '%s'" % (d, pattern))

        positions = set()

        pattern_length = len(pattern)
        min_matches = len(pattern) - d
        pattern = tuple(pattern)

        for i in range(0, len(self) - len(pattern) + 1):
            matched = sum(map(lambda e: e[0] == e[1], zip(pattern, self[i:i + pattern_length])))
            if matched >= min_matches:
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
            removed = self[i - 1:i + k - 1]
            introduced = self[i + region - k:i + region]
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

    @staticmethod
    def is_similar(str1, str2, max_diff):
        """ Silly k-mers of the same lenght comparison with up to max_distance modifications
        @param str kmer_a:
        @param str kmer_b:
        @param str max_distance:
        @return: str
        """
        if len(str1) != len(str2):
            raise ValueError('Cannot compare kmers of different length')
        if max_diff == 0 or not len(str1):
            return str1.lower() == str2.lower()
        else:
            str1 = str1.lower()
            str2 = str2.lower()

            for shift in range(-max_diff, max_diff + 1):
                if shift < 0:
                    shifted = str1[-shift:] + ' ' * (-shift)
                elif shift == 0:
                    shifted = str1
                else: # shift > 0
                    shifted = ' ' * shift + str1[:-shift]

                matched = sum(c[0] == c[1] for c in zip(shifted, str2))
                if (len(str1) - max_diff) <= matched:
                    return True
            return False

    @staticmethod
    def is_similar_simple(str1, str2, max_diff):
        """ Silly k-mers of the same lenght comparison with up to max_distance modifications
        @param str kmer_a:
        @param str kmer_b:
        @param str max_distance:
        @return: str
        """
        if len(str1) != len(str2):
            raise ValueError('Cannot compare kmers of different length')
        if max_diff == 0 or not len(str1):
            return str1.lower() == str2.lower()
        else:
            str1 = str1.lower()
            str2 = str2.lower()

            matched = sum(c[0] == c[1] for c in zip(str1, str2))
            if (len(str1) - max_diff) <= matched:
                return True

            return False

    @staticmethod
    def is_similar_but_not_equal(str1, str2, max_diff):
        if str1 == str2:
            return False
        else:
            return Genome.is_similar(str1, str2, max_diff)

    def kmer_nucleotide_frequencies(self, k):
        """ Find nucleotide frequencies of all k-mers in genome """
        frequencies = []
        for i in range(k):
            frequencies.append({'c': 0, 't': 0, 'a': 0, 'g': 0})

        for i in range(0, self.kmers_of(k)):
            for j, nucleotide in enumerate(self[i:i + k]):
                frequencies[j][nucleotide.lower()] += 1

        return frequencies

    def kmer_nucleotide_probabilities(self, k):
        """ Find probabilities of nucleotide appearance in positions from 0 to k
        @param k: int
        @return: list
        """
        total_kmers = float(self.kmers_of(k))
        probabilities = []

        for frequencies in self.kmer_nucleotide_frequencies(k):
            probabilities.append(dict(map(lambda nuc: (nuc[0], nuc[1] / total_kmers), frequencies.iteritems())))

        return probabilities

    def translate(self):
        """
        @return: bio.RNA
        """
        return bio.RNA(self)
