"""
    libextract.coretools
    ~~~~~~~~~~~~~~~~~~~~

    Implements the core utilities and functions in which
    libextract is built around.
"""

from collections import Counter
from functools import wraps
from lxml.html import parse, HTMLParser


def histogram(iterable):
    """
    Given an *iterable* of key-to-value pairs, sum up the
    `value` for each `key` and return a counter/histogram.
    """
    hist = Counter()
    for key, score in iterable:
        hist[key] += score
    return hist


def argmax(counter):
    """
    Returns the most common element in a *counter*.
    """
    return counter.most_common(1)[0]


def pipeline(data, functions):
    """
    Pipes *functions* onto a given *data*, where the result
    of the previous function is fed to the next function.
    """
    for item in functions:
        data = item(data)
    return data


def prunes(selector):
    """
    Given a *selector*, returns a function which selects
    nodes from a given etree and then yields the result
    of calling the wrapped function on each node.
    """
    def decorator(fn):
        @wraps(fn)
        def mapper(etree):
            for node in etree.xpath(selector):
                yield fn(node)
        return mapper
    return decorator


def debug(fn):
    """
    This decorator will hook into a function's out
    and print out the output value.

    @debug
    @node_processor
    def if_table(node):
        if node.tag == "table":
            table = table_json(node)
            for e, row in enumerate(table['Average female height']):
                s = re.split("^(.*)cm", row)
                table['Average female height'][e] = "".join(s[:2]).strip()
            return table
        else:
            return node

    Sample output:
    
    decorator running ... output: <generator object filter_tags...>)
    Press <Enter> to continue
    decorator running ... output:
    {
        'Sample population / age range': [
                u'20\u201329',
                u'19\u201349',
                '17 (healthy)',
                ...]
    }
    Press <Enter> to continue
    decorator running ... output: <Element ol at 0x6111778>)
    Press <Enter> to continue
    decorator running ... output: <Element span at 0x61036d8>)
    Press <Enter> to continue
    decorator running ... output: <Element div at 0x38a4bd8>)
    Press <Enter> to continue
    decorator running ... output: <Element ul at 0x3af64a8>)
    Press <Enter> to continue
    """
    @wraps(fn)
    def decorator(*args):
        print("{0} running ... output: {1})".format(fn.__name__, args))

        input("Press <Enter> to continue")

        data = fn(*args)
        for d in data:
            print("{0} running ... output: {1})".format(fn.__name__, d))
            input("Press <Enter> to continue")

        yield data

    return decorator


def node_processor(fn):
    """
    Use this decorator if you would like to create your own
    node processor. For example, if you would like to
    execute a custom function if a node happens to be a
    <table>, <ul>, <ol> element:

        @node_processor
        def if_table(node):
            if node.tag == "table":
                return table_json(node)
            else:
                return node

        @node_processor
        def if_list(node):
            if node.tag == "ul" or node.tag == "ol":
                return [li.text_content() for li in node.iter('li')]
            else:
                return node
        ...


        strategy = (parse_html,
                    basket_node_and_counter,
                    node_counter_argmax,
                    sort_best_pairs,
                    filter_tags,
                    if_table,
                    if_list)
    """
    wraps(fn)
    def decorator(nodes):
        for node in nodes:
            try:
                yield fn(node)
            except(AttributeError):
                yield node
    return decorator


def get_node(pair):
    """
    Given a (node, text_length or collections.Counter)
    *pair*, returns the node.
    """
    node, _ = pair
    return node


def parse_html(fileobj, encoding='utf-8'):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding=encoding,
                            remove_blank_text=True))
