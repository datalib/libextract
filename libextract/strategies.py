# TODO: circular dependencies?
from .coretools import histogram, argmax
from .html import get_etree, get_pairs, get_final_text


_BASE = (get_etree, get_pairs, histogram, argmax)

ARTICLE_TEXT = _BASE + (get_final_text,)
ARTICLE_NODE = _BASE + (lambda (n, _): n,)


# shortcuts
AT = ARTICLE_TEXT
AN = ARTICLE_NODE
