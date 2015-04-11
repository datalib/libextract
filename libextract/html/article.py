from operator import itemgetter
from libextract.html import parse_html
from libextract.coretools import histogram, argmax
from libextract.html.xpaths import FILTER_TEXT
from libextract.pruners import subnode_textlen_pruner

get_node = itemgetter(0)


def get_text(node):
    """
    Gets the text contained within the children node
    of a given *node*, joined by a space.
    """
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (parse_html, subnode_textlen_pruner, histogram, argmax, get_node)
