from collections import Counter


def histogram(iterable):
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist


def argmax(histogram):
    return histogram.most_common(1)[0]


def pipeline(data, functions):
    for item in functions:
        data = item(data)
    return data
