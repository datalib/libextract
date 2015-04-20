"""
"""
from functools import wraps
from heapq import nlargest
from statscounter import StatsCounter


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
    Generates *nodes* using etree.xpath
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
            print("maximize.decorator.iterator", top, fn(*args), args)
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
### Not yet tested... ###
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

