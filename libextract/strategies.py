"""
    libextract.strategies
    ~~~~~~~~~~~~~~~~~~~~~

    Exports the strategies for tabular/article data
    extraction.
"""

from libextract.tabular import STRATEGY as TABULAR
from libextract.article import STRATEGY
from libextract.formatters import get_text

ARTICLE_NODE = STRATEGY
ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
