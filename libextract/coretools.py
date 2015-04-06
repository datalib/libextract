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


def memoized(prod):
    cache = {}
    def func(arg):
        if arg not in cache:
            cache[arg] = prod(arg)
        return cache[arg]
    return func
