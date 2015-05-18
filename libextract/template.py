from operator import itemgetter
from heapq import nlargest


class Extractor(object):
    xpath = None
    metric = staticmethod(len)
    rank_pair = staticmethod(itemgetter(1))

    def __init__(self, count=5):
        self.count = count

    def select(self, etree):
        return etree.xpath(self.xpath)

    def measure(self, nodes):
        for node in nodes:
            yield node, self.metric(node)

    def rank(self, pairs):
        return nlargest(self.count, pairs, key=self.rank_pair)

    def finalise(self, ranked):
        return ranked

    def compile_pipeline(self):
        return [
            self.select,
            self.measure,
            self.rank,
            self.finalise,
        ]
