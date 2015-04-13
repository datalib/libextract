"""
    libextract.tabular
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting tabular
    nodes from documents.
"""

from heapq import nlargest
from libextract.coretools import argmax, parse_html
from libextract.baskets import basket_node_and_counter


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable
    of (node, collections.Counter) *pairs*.
    """
    for node, counter in pairs:
        yield node, argmax(counter)


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    _, (_, score) = pair
    return score


def weighted_score(pair, favours=frozenset(['table']), k=1.5):
    """
    Return the score for a given (node, (tag, frequency))
    *pair* favouring nodes which tags are contained in
    *favours* by multiplying their scores by *k*.
    """
    parent, (_, score) = pair
    if parent.tag in favours:
        return k * score
    return score


def sort_best_pairs(pairs, top=5, sortfunc=select_score):
    """
    Given an iterable of (node, (tag, frequency)) *pairs*,
    obtain the *top* best pairs according to *sortfunc*.
    """
    return nlargest(top, pairs, key=sortfunc)


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
            basket_node_and_counter,
            node_counter_argmax,
            sort_best_pairs,
            filter_tags)
