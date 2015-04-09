# TODO: circular dependencies?
from .html.tabular import STRATEGY as TABULAR
from .html.text import STRATEGY, get_final_text

ARTICLE_TEXT = STRATEGY + (get_final_text,)
ARTICLE_NODE = STRATEGY + (lambda (n, _): n,)
