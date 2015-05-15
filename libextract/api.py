"""
libextract.ors module contains built-in extractor
methods for the most common data extracting use
cases: article text and tabular data extraction

Warning! These extractors will return the HTML
element(s) likely containing the desired data.
Libextract will not clean the data.
"""
from functools import partial

from .core import parse_html, pipeline
from .generators import selects, maximize
from .xpaths import PARENT_NODES, TEXT_NODES
from .metrics import text_length
from statscounter import StatsCounter

DEFAULT_ENC = 'utf-8'


def articles(document, encoding=DEFAULT_ENC, count=5):
    """
    Given an html *document*, and optionally the *encoding*,
    and the number of predictions (*count*) to return
    (in descending rank) *articles* returns a list of HTML nodes
    likely containing the main article of a given website.

    The extraction algorithm is based of text length.
    Refer to rodricios.github.io/eatiht for an in-depth
    explanation.
    """
    @maximize(count, lambda x: x[1])
    @selects(TEXT_NODES) # uses text-extracting xpath
    def predictor(node):
        return node.getparent(), text_length(node)

    enc_parse = partial(parse_html, encoding=encoding)
    return pipeline(document, (parse_html, predictor,))


def tabular(document, encoding=DEFAULT_ENC, count=5):
    """
    Given an html *document*, and optionally the *encoding*,
    and the number of predictions (*count*) to return
    (in descending rank) *tabular* returns a list of HTML
    nodes likely containing "tabular" data (ie. table,
    and table-like elements).
    """
    # "maximize" is a sorting function.
    @maximize(count, lambda x: x[1].max())
    @selects(PARENT_NODES) # uses table-extracting xpath
    def predictor(node):
        return node, StatsCounter([child.tag for child in node])

    enc_parse = partial(parse_html, encoding=encoding)
    return pipeline(document, (enc_parse, predictor,))
