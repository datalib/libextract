"""
    libextract.strategies
    ~~~~~~~~~~~~~~~~~~~~~

    Exports trategies for tabular/article data
    extraction.
"""

from .tabular import STRATEGY as TABULAR
from .formatters import get_text
from .baskets import parent_length_pairs
from .coretools import histogram, argmax, parse_html, get_node


__all__ = ('ARTICLE_NODE', 'ARTICLE_TEXT', 'TABULAR',)


ARTICLE_NODE = (parse_html,
                parent_length_pairs,
                histogram,
                argmax,
                get_node)

ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
