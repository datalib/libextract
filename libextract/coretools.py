from collections import Counter
from functools import wraps
from lxml.html import parse, HTMLParser


def histogram(iterable):
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist


def argmax(counter):
    return counter.most_common(1)[0]


def pipeline(data, functions):
    for item in functions:
        data = item(data)
    return data


def prunes(selector):
    def decorator(fn):
        @wraps(fn)
        def mapper(etree):
            for node in etree.xpath(selector):
                yield fn(node)
        return mapper
    return decorator


def parse_html(fileobj, encoding='utf-8'):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding=encoding,
                            remove_blank_text=True))
