def most_repeated(size, genome):
    result = {}
    for i in range(0, len(genome) - size + 1):
        part = genome[i:i+size]
        if part in result:
            result[part] += 1
        else:
            result[part] = 1
    return result


def most_repeated_top(number, size, genome):
    mr = most_repeated(size, genome)
    return sorted(mr, key=mr.get, reverse=True)[0:number]


def reverse_complement(genome):
    return ''.join(map(
        lambda s: {'a': 't', 'g': 'c', 'c': 'g', 't': 'a', 'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}[s],
        genome[::-1])
    )
