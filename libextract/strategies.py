#TODO: circular dependencies?
from .coretools import histogram, argmax
from .html import get_etree, get_pairs, get_final_text


ARTICLE_TEXT = (get_etree, get_pairs, histogram, argmax, get_final_text)

ARTICLE_NODE = (get_etree, get_pairs, histogram, argmax, lambda (n, _): n)

#shortcuts
AT = ARTICLE_TEXT
AN = ARTICLE_NODE
