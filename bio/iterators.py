def chunker(sequence, chunk_size):
    for x in range(0, len(sequence), chunk_size):
        yield sequence[x:x+chunk_size]
