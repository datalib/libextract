from heapq import nlargest
from libextract.coretools import Counter
from libextract.html import get_etree


SELECT_ALL = '//*'


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
    to child node frequencies (collections.Counter) length pairs.
    """
    for node in etree.xpath(SELECT_ALL):
        if len(node):
            yield node, children_counter(node)


def node_counter_argmax(pairs, top=1):
    for node, children in pairs:
        yield node, children.most_common(top)


def sort_best_pairs(pairs, limit=5):
    return nlargest(
        limit,
        pairs,
        key=lambda (node, children): sum(k[1] for k in children),
        )


STRATEGY = (get_etree,
            get_node_counter_pairs,
            node_counter_argmax,
            sort_best_pairs)
