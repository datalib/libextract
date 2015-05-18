from .core import histogram
from .extractor import Extractor
from .metrics import text_length
from .xpaths import TEXT_NODES


def parent_length_pairs(results):
    for node, metric in results:
        yield node.getparent(), metric


class ArticleExtractor(Extractor):
    xpath = TEXT_NODES
    metric = staticmethod(text_length)

    def measure(self, nodes):
        return parent_length_pairs(Extractor.measure(self, nodes))

    def rank(self, measured):
        return histogram(measured).most_common(self.count)
