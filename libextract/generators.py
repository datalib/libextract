"""
    libextract.generators
    ~~~~~~~~~~~~~~~~~~~~~

    This module attempts to refactor the many for-loop
    node-yielding methods found in the previous implementation
    of libextract.

    The main decorators to try out are *iters*, *selects*,
    and *maximize*. With just *selects* and *maximize*, users
    can recreate the TABULAR and ARTICLE_TEXT strategies from
    the previous implementation of libextract.

    ##########################################
    ################## DEMO ##################
    ##########################################

    from requests import get
    opensecrets = "http://en.wikipedia.org/wiki/Human_height"
    r = get(opensecrets) # make request, receive response from site

    from libextract.core import extract, pipeline
    from libextract.generators import selects, maximize
    from statscounter import StatsCounter

    from functools import partial

    @maximize(5, lambda x: x[1].max())
    @selects("//*/..")
    def group_parents_children(node):
        return node, StatsCounter([child.tag for child in node])


    @maximize(5, lambda x: x[1])
    @selects("text")
    def group_nodes_texts(node):
        return node.getparent(), len(" ".join(node.text_content().split()))


    extract = partial(extract, encoding='utf-8')

    tables = pipeline(r.content, (extract, group_parents_children,))

    text = pipeline(r.content, (extract, group_nodes_texts,))
"""

from functools import wraps
from heapq import nlargest

from .metrics import StatsCounter


def iters(*tags):
    """
    Generates *nodes* using etree.iter
    """
    tags = set(tags)
    @wraps(iters)
    def decorator(fn):
        @wraps(fn)
        def iterator(node, *args):
            for elem in node.iter(*tags):
                yield fn(elem,*args)
        return iterator
    return decorator


def selects(xpath):
    """
    Generates *nodes* using etree.xpath.

    ###USEFUL XPATHS###

    To get html nodes with text:
    '//*[not(self::script or self::style)]/text()[normalize-space()]/..'

    To get anchor tags (<a>):
    '//a'
    """
    @wraps(selects)
    def decorator(fn):
        @wraps(fn)
        def selector(node, *args):
            for n in node.xpath(xpath):
                yield fn(n)
        return selector
    return decorator


def select_score(pair):
    """
    Select the frequency in a (node, (tag, frequency))
    *pair*, which is used as the score.
    """
    if isinstance(pair, tuple):
        if isinstance(pair[1], StatsCounter):
            return pair[1].max()
    else:
        _, (_, score) = pair
        return score


def maximize(top=5, max_fn=select_score):
    """
    Selects the *top* nodes using suing maximizing
    function (*max_fn*).
    """
    @wraps(maximize)
    def decorator(fn):
        @wraps(fn)
        def iterator(*args):
            return nlargest(top, fn(*args), key=max_fn)
        return iterator
    return decorator


def processes(*tags):
    tags = set(tags)
    @wraps(processes)
    def decorator(fn):
        @wraps(fn)
        def processor(nodes,*args):
            for node in nodes:
                #yield fn(n) if n.tag in tags else n
                if node.tag in tags:
                    yield fn(node, *args)
                    continue
                yield node, args
        return processor
    return decorator

#########################
### Very experimental ###
#########################

def filter_tags(fn):
    """
    Given iterable of (node, (tag, frequency)) *pairs*,
    clean up the node by filtering out child nodes whose
    tag names != tag.
    """
    @wraps(fn)
    def decorator(pairs):
        for node, (tag, _) in pairs:
            for child in node:
                if fn(node, tag, child):
                    node.remove(child)
            yield node
    return decorator

def conditions(fn):
    @wraps(fn)
    def decorator(nodes, *args):
        for node in nodes:
            if fn(node, *args):
                yield node
    return decorator
