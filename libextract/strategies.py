from libextract.tabular import STRATEGY as TABULAR
from libextract.article import STRATEGY, get_text

ARTICLE_NODE = STRATEGY
ARTICLE_TEXT = ARTICLE_NODE + (get_text,)
