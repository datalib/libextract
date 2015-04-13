"""
    libextract.article
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting textual
    data from articles.
"""

from libextract.baskets import basket_parent_and_lengths
from libextract.coretools import histogram, argmax, prunes, \
                    parse_html, get_node


STRATEGY = (parse_html,
            basket_parent_and_lengths,
            histogram,
            argmax,
            get_node)
