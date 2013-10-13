def most_repeated(size, genome):
    result = {}
    for i in range(0, len(genome) - size + 1):
        part = genome[i:i+size]
        if part in result:
            result[part] += 1
        else:
            result[part] = 1
    return result