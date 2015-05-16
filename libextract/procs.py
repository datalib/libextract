from heapq import nlargest
from operator import itemgetter


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


def get_largest(n, key=itemgetter(1)):
    def largest(results):
        return nlargest(n, results, key=key)
    return largest
