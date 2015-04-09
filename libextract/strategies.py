# TODO: circular dependencies?
from .html.tabular import STRATEGY as TABULAR
from .html.article import STRATEGY, get_text

ARTICLE_TEXT = STRATEGY + (get_text,)
ARTICLE_NODE = STRATEGY + (lambda (n, _): n,)
