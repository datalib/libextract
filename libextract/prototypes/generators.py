"""
"""
from functools import wraps
from types import GeneratorType


def iterates(node,*tags):
    for elem in node.iter(*tags):
        yield elem

def iters(*tags):
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
    @wraps(selects)
    def decorator(fn):
        @wraps(fn)
        def selector(node, *args):
            for n in node.xpath(xpath):
                yield fn(n)
        return selector
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
                    yield fn(node)
                    continue
                yield node
        return processor
    return decorator
