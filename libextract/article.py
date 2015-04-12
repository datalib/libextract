"""
    libextract.article
    ~~~~~~~~~~~~~~~~~~
    Implements extraction strategy for extracting textual
    data from articles.
"""


from operator import itemgetter
from libextract.coretools import histogram, argmax, prunes, parse_html
from libextract.metrics import text_length
from libextract.formatters import get_text


NODES_WITH_TEXT = '//*[not(self::script or self::style)]/\
                     text()[normalize-space()]/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'


@prunes(NODES_WITH_TEXT)
def get_node_length_pairs(node):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    return node.getparent(), text_length(node)


get_node = itemgetter(0)


STRATEGY = (parse_html,
            get_node_length_pairs,
            histogram,
            argmax,
            get_node)
