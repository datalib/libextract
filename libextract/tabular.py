from .xpaths import PARENT_NODES
from .metrics import count_children
from .procs import select, rank_with, get_largest


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
        for child in node:
            if child.tag != tag:
                node.remove(child)
        yield node


def build_strategy(count=5):
    return (
        select(PARENT_NODES),
        rank_with(count_children),
        node_counter_argmax,
        get_largest(count, key=select_score),
        filter_tags,
    )
