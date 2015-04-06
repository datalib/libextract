from collections import Counter


def highest_scoring(iterable):
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist.most_common(1)[0][0]


def pipeline(data, functions):
    for item in functions:
        data = item(data)
    return data
