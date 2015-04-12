"""
    libextract.article
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting textual
    data from articles.
"""

from libextract.coretools import histogram, argmax, prunes, parse_html
from libextract.baskets import basket_parent_and_lengths

def get_node(pair):
    """
    Given a (node, text_length) *pair*, returns the
    node.
    """
    node, _ = pair
    return node


STRATEGY = (parse_html,
            basket_parent_and_lengths,
            histogram,
            argmax,
            get_node)
