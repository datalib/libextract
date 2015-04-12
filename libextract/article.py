"""
    libextract.article
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting textual
    data from articles.
"""

from libextract.coretools import histogram, argmax, prunes, parse_html
from libextract.metrics import text_length
from libextract.xpaths import NODES_WITH_TEXT


@prunes(NODES_WITH_TEXT)
def get_node_length_pairs(node):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    return node.getparent(), text_length(node)


def get_node(pair):
    """
    Given a (node, text_length) *pair*, returns the
    node.
    """
    node, _ = pair
    return node


STRATEGY = (parse_html,
            get_node_length_pairs,
            histogram,
            argmax,
            get_node)
