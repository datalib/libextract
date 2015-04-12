from operator import itemgetter
from libextract.html import parse_html
from libextract.coretools import histogram, argmax
from libextract.html.xpaths import FILTER_TEXT
from libextract.pruners import prune_by_text_length


get_node = itemgetter(0)


def get_text(node):
    """
    Gets the text contained within the children node
    of a given *node*, joined by a space.
    """
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (parse_html,
            prune_by_text_length,
            histogram,
            argmax,
            get_node)
