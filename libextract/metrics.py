"""
    libextract.metrics
    ~~~~~~~~~~~~~~~~~~

    Implements "quantifying functions"- each function expects
    a lxml.html.HtmlElement (sometimes *._ElementTree) *node*
    and the function will return either a numerical type or a
    Counter.
"""

from collections import Counter


def text_length(node):
    """
    Returns the length of the text contained within
    a given *node*.
    """
    text = node.text
    return len(' '.join(text.split())) if text else 0


def count_children(node):
    """
    Returns the a collections.Counter object measuring the
    frequenies of the children nodes (by tag name) contained
    within a given *node*.
    """
    return Counter([child.tag for child in node])
