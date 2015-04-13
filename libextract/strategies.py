"""
    libextract.strategies
    ~~~~~~~~~~~~~~~~~~~~~

    Exports the strategies for tabular/article data
    extraction.
"""

from libextract.tabular import STRATEGY as TABULAR
from libextract.formatters import get_text
from libextract.baskets import parent_length_pairs_of
from libextract.coretools import histogram, argmax, parse_html, get_node
from libextract.xpaths import NODES_WITH_TEXT


__all__ = ('ARTICLE_NODE', 'ARTICLE_TEXT', 'TABULAR',)


ARTICLE_NODE = (parse_html,
                parent_length_pairs_of(NODES_WITH_TEXT),
                histogram,
                argmax,
                get_node)

ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
