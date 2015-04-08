from collections import Counter


def histogram(iterable):
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist


def argmax(histogram):
    return histogram.most_common(1)[0]


def above_threshold(score):
    def proc(pairs):
        for key, value in pairs:
            if value >= score:
                yield key, value
    return proc


def pipeline(data, functions):
    for item in functions:
        data = item(data)
    return data
