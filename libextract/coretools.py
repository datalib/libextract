from collections import Counter


def histogram(iterable):
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist


def argmax(counter):
    return counter.most_common(1)[0]


def pipeline(data, functions):
    for item in functions:
        data = item(data)
    return data
