from .extractor import Extractor
from .metrics import count_children
from .xpaths import PARENT_NODES


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable
    of (node, StatsCounter) *pairs*.
    """
    for node, counter in pairs:
        yield node, counter.argmax()


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    _, (_, score) = pair
    return score


def filter_tags(pairs):
    """
    Given iterable of (node, (tag, frequency)) *pairs*,
    clean up the node by filtering out child nodes whose
    tag names != tag.
    """
    for node, (tag, _) in pairs:
        for child in list(node):
            if child.tag != tag:
                node.remove(child)
        yield node


class TabularExtractor(Extractor):
    xpath = PARENT_NODES
    metric = count_children
    rank_pair = select_score

    def rank(self, pairs):
        pairs = node_counter_argmax(pairs)
        return Extractor.rank(self, pairs)

    def finalise(self, pairs):
        return filter_tags(pairs)
