from operator import itemgetter
from libextract.html import parse_html
from libextract.coretools import histogram, argmax
from libextract.html._xpaths import NODES_WITH_TEXT, FILTER_TEXT
from libextract.quantifiers import text_length


def get_node_length_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    for node in etree.xpath(NODES_WITH_TEXT):
        yield node.getparent(), text_length(node)


get_node = itemgetter(0)


def get_text(node):
    """
    Gets the text contained within the children node
    of a given *node*, joined by a space.
    """
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (parse_html, get_node_length_pairs, histogram, argmax, get_node)
