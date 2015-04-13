"""
    libextract.tabular
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting tabular
    nodes from documents.
"""

from heapq import nlargest
from libextract.baskets import node_children_pairs_of
from libextract.coretools import argmax, parse_html
from libextract.xpaths import NODES_WITH_CHILDREN


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable
    of (node, collections.Counter) *pairs*.
    """
    for node, counter in pairs:
        if counter:
            yield node, argmax(counter)


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    _, (_, score) = pair
    return score


def weighted_score(favours, k=1.5):
    """
    Return a function that gets the frequency for a given
    (node, (tag, frequency)) *pair* favouring nodes which
    tags are contained in *favours* by multiplying their
    scores by *k*.
    """
    def scorefunc(pair):
        node, (_, score) = pair
        if node.tag in favours:
            return k * score
        return score
    return scorefunc


def get_top_pairs(top, sortfunc=select_score):
    """
    Returns a function that sorts an iterable of
    (node, (tag, frequency)) pairs using *sortfunc*,
    and obtains the *top* best pairs.
    """
    def sort_best_pairs(pairs):
        return nlargest(top, pairs, key=sortfunc)
    return sort_best_pairs


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


STRATEGY = (parse_html,
            node_children_pairs_of(NODES_WITH_CHILDREN),
            node_counter_argmax,
            get_top_pairs(5),
            filter_tags)
