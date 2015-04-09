from libextract.html import get_etree
from libextract.coretools import histogram, argmax


NODES_WITH_TEXT = '//*[not(self::script or self::style)]/\
                     text()[normalize-space()]/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'


def node_text_length(node):
    """
    Returns the length of the text contained within
    a given *node*.
    """
    return len(' '.join(node.text_content().split()))


def get_node_length_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    for node in etree.xpath(NODES_WITH_TEXT):
        yield node.getparent(), node_text_length(node)


def get_final_text(pair):
    """
    Gets the text contained within the children node
    of a given node and text length *pair*, joined by
    a space.
    """
    node, _ = pair
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (get_etree, get_node_length_pairs, histogram, argmax)
