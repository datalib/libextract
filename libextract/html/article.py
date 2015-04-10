from operator import itemgetter
from libextract.html import parse_html
from libextract.coretools import histogram, argmax
from libextract.html._xpaths import NODES_WITH_TEXT, FILTER_TEXT


def node_text_length(node):
    """
    Returns the length of the text contained within
    a given *node*.
    """
    text = node.text
    return len(' '.join(text.split())) if text else 0


def get_node_length_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    for node in etree.xpath(NODES_WITH_TEXT):
        yield node.getparent(), node_text_length(node)


get_node = itemgetter(0)


def get_text(node):
    """
    Gets the text contained within the children node
    of a given *node*, joined by a space.
    """
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (parse_html, get_node_length_pairs, histogram, argmax, get_node)
