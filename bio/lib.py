import re
import networkx as nx

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

    def most_repeated_rough(self, k, d):
        mr = self.most_repeated(k)

        gr = nx.Graph()

        for k_mer in mr.iterkeys():
            gr.add_node(k_mer, {'count': mr[k_mer]})

        for node_a in gr.nodes_iter():
            for node_b in gr.nodes_iter():
                if not gr.has_edge(node_a, node_b) and Genome.is_similar_but_not_equal(node_a, node_b, d):
                    gr.add_edge(node_a, node_b)

        top_result = -1
        top_set = []

        for clique in nx.find_cliques(gr):
            current_count = sum(gr.node[node]['count'] for node in clique)
            if current_count == top_result:
                top_set.append(clique)
            elif current_count > top_result:
                top_result = current_count
                top_set = clique

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
            matched = sum(map(lambda e: e[0] == e[1], zip(pattern, self[i:i+pattern_length])))
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
            for shift in range(-max_diff, max_diff + 1):
                if shift < 0:
                    shifted = str1[-shift:] + ' '*(-shift)
                elif shift == 0:
                    shifted = str1
                else: # shift > 0
                    shifted = ' '*shift + str1[:-shift]

                matched = sum(c[0] == c[1] for c in zip(shifted, str2))
                if (len(str1) - max_diff) <= matched:
                    return True
            return False

    @staticmethod
    def is_similar_but_not_equal(str1, str2, max_diff):
        if str1 == str2:
            return False
        else:
            return Genome.is_similar(str1,  str2, max_diff)
