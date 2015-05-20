from .extractor import Extractor
from .metrics import count_children
from .xpaths import PARENT_NODES


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable
    of (node, StatsCounter) *pairs*.
    """
    for node, counter in pairs:
        yield node, counter.most_common()[0]


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    _, (_, score) = pair
    return score


class TabularExtractor(Extractor):
    """
    An Extractor that extracts the most probable
    nodes that represent tabular data.
    """

    xpath = PARENT_NODES
    metric = staticmethod(count_children)
    rank_pair = staticmethod(select_score)

    def rank(self, pairs):
        pairs = node_counter_argmax(pairs)
        return Extractor.rank(self, pairs)
