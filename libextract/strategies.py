"""
    libextract.strategies
    ~~~~~~~~~~~~~~~~~~~~~

    Exports the strategies for tabular/article data
    extraction.
"""

from libextract.tabular import STRATEGY as TABULAR
from libextract.formatters import get_text
from libextract.baskets import basket_parent_and_lengths
from libextract.coretools import histogram, argmax, parse_html, get_node


__all__ = ('ARTICLE_NODE', 'ARTICLE_TEXT', 'TABULAR',)


ARTICLE_NODE = (parse_html,
                basket_parent_and_lengths,
                histogram,
                argmax,
                get_node)

ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
