"""
    libextract.formatters
    ~~~~~~~~~~~~~~~~~~~~~

    Formats the results of extraction into serializable
    representations, e.g. JSON, text.
"""

from functools import partial
try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest
from libextract.xpaths import FILTER_TEXT


UNLIMITED = float('NaN')


def get_text(node):
    """
    Gets the text contained within the children node
    of a given *node*, joined by a space.
    """
    return ' '.join(node.xpath(FILTER_TEXT))


def split_node_attr(node, attr):
    """
    Given a *node*, split the *attr* of the node
    into a list of strings, suitable for id/class
    handling.
    """
    return (node.get(attr) or '').split()


get_node_id = partial(split_node_attr, attr='id')
get_node_class = partial(split_node_attr, attr='class')


def node_json(node, depth=0):
    """
    Given a *node*, serialize it and recursively
    serialize it's children to a given *depth*.
    Note that if the *depth* runs out (goes to 0),
    the children key will be ``None``.
    """
    return {
        'xpath': node.getroottree().getpath(node),
        'class': get_node_class(node),
        'text': node.text,
        'tag': node.tag,
        'id': get_node_id(node),
        'children': (
            [node_json(n, depth-1) for n in node] if depth else None
        ),
    }


def chunks(iterable, size):
    """
    Yield successive chunks of *size* from a given
    *iterable*, filling the unfilled chunks with
    None.
    """
    args = [iter(iterable)] * size
    for row in zip_longest(*args, fillvalue=None):
        yield list(row)


def extract_tabular_node(node, tag):
    """
    Given a *node*, yield all of the child nodes in depth
    first order, that matches the given *tag*.
    """
    for elem in node.iter(tag):
        yield ' '.join(elem.text_content().split())


get_table_headings = partial(extract_tabular_node, tag='th')
get_table_rows = partial(extract_tabular_node, tag='td')


def table_json(node):
    """
    Given a table *node* (ie. <table>), return a dictionary
    of key-value pairs, where the key is the heading and the
    value is a list of rows.
    """
    headings = list(get_table_headings(node))
    rows = list(chunks(get_table_rows(node), len(headings)))
    return {heading: [row[col] for row in rows]
            for col, heading in enumerate(headings)}


def table_list(node):
    """
    Given a table *HtmlElement* (ie. <table>), return
    a list of lists, where the first list contains the
    table headings, and the subsequent lists contain
    rows of data.
    """
    headings = list(get_table_headings(node))
    rows = get_table_rows(node)
    table = [headings]
    table.extend(chunks(rows, len(headings)))
    return table


def ul_ol_list(node):
    """
    Given an un/ordered list *HtmlElement* (ie. <ul>|<ol>),
    return a list, where the first item is be the id and classes
    of the *node*, and the subsequent items contain the inner
    text of the list.
    """
    attrs = get_node_id(node)
    attrs.extend(get_node_class(node))
    yield attrs
    for elem in node.iter('li'):
        yield elem.text_content()
