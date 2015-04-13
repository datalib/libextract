"""
    libextract.baskets
    ~~~~~~~~~~~~~~~~~~
    Implements functions that "basket" pruned nodes.

    The intent of this library can be understood with
    by making an analogy with farmers who want to pick
    the best fruit. Instead of meticulously reviewing
    every fruit in his orchard, and attempting to
    mentally record the location of the last best fruit,
    the farmer designs special "baskets".

    These baskets allow the farmer to calmly traverse
    through his orchard, and unlike before, the farmer
    can simply eyeball those fruits that look good.

    This procedure works with the caveat that there must
    exist some later procedure that will do execute the
    reviewing stage for the farmer later.

    This module provides some common basketting techniques
    that help with predicting tabular data and article
    text.
"""

from libextract.coretools import prunes
from libextract.metrics import text_length, count_children
from libextract.xpaths import NODES_WITH_TEXT, SELECT_ALL


@prunes(NODES_WITH_TEXT)
def basket_parent_and_lengths(node):
    """
    Given an *etree*, returns an iterable of parent node
    to child nodes text length pairs.
    """
    return node.getparent(), text_length(node)


@prunes(SELECT_ALL)
def basket_node_and_counter(node):
    """
    Given an *etree*, returns an iterable of node to
    child node frequencies (collections.Counter) pairs.
    """
    return node, count_children(node)
