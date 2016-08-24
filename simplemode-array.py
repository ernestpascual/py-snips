def arrayMode(sequence):
    from collections import Counter
    data = Counter(sequence)
    return data.most_common(1)[0][0]

