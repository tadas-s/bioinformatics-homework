def chunker(sequence, chunk_size):
    for x in range(0, len(sequence), chunk_size):
        yield sequence[x:x+chunk_size]


def kmers(sequence, k):
    if k < 1:
        raise ValueError("There is no such thing as %s-mer" % (k,))

    for i in range(0, max(0, len(sequence) - k + 1)):
        yield sequence[i:i + k]
