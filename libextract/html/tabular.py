from operator import itemgetter
from heapq import nlargest
from libextract.coretools import Counter
from libextract.html import parse_html
from libextract.html._xpaths import SELECT_ALL

#TODO: Consolidate get_pairs functions
#TODO: Converge on get_*, filter_*
#TODO: Better yet, decide on "meta/pipelining language"


def children_counter(node):
    """
    Returns the a collections.Counter object measuring the
    frequenies of the children nodes (by tag name) contained
    within a given *node*.
    """
    return Counter([child.tag for child in node])


def get_node_counter_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to child node frequencies (collections.Counter) pairs.
    """
    for node in etree.xpath(SELECT_ALL):
        if len(node):
            yield node, children_counter(node)


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable of
    (node, collections.Counter) *pairs*.
    """
    for node, children in pairs:
        yield node, children.most_common(1)[0]


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    _, (_, score) = pair
    return score


def weighted_score(pair, favours={'table'}, k=1.5):
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
    return nlargest(limit, pairs, key=sortfunc)


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


STRATEGY = (parse_html,
            get_node_counter_pairs,
            node_counter_argmax,
            sort_best_pairs,
            filter_tags)
