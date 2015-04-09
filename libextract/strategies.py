# TODO: circular dependencies?
from .html.tabular import STRATEGY as TABULAR
from .html.article import STRATEGY, get_text

ARTICLE_NODE = STRATEGY
ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
