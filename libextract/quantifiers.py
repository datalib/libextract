from __future__ import absolute_import
"""
A submodule providing 'quantifying' functions.

The protocol that's followed is each function expects a "node"
of type lxml.html.HtmlElement (sometimes *._ElementTree), and
the function will return either a numerical type or a Counter
where the key=<node> and value=<numerical>
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
