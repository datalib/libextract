from heapq import nlargest
from operator import itemgetter
from .core import sum_metrics


def select(xpath):
    def selector(node):
        for child in node.xpath(xpath):
            yield child
    return selector


def rank_with(metric):
    def ranker(nodes):
        for node in nodes:
            yield node, metric(node)
    return ranker


def histogram(function):
    def hist(results):
        return sum_metrics(function(results))
    return hist


def get_largest(n, key=itemgetter(1)):
    def largest(results):
        return nlargest(n, results, key=key)
    return largest


def most_common(n):
    def largest(counter):
        return counter.most_common(n)
    return largest
