"""
    libextract.formatters
    ~~~~~~~~~~~~~~~~~~~~~

    Formats the results of extraction into serializable
    representations, e.g. JSON, text.
"""

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


def split_node_attr(attr):
    """
    Returns a function that, given a *node*, splits
    the *attr* of the node into a list of strings.
    """
    def splitter(node):
        return (node.get(attr) or '').split()
    return splitter


get_node_id = split_node_attr('id')
get_node_class = split_node_attr('class')


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


def tabular_node_extractor(tag):
    """
    Returns a function that yields all of the child
    nodes of a given *node* in depth first order, that
    matches the given *tag*.
    """
    def extract(node):
        for elem in node.iter(tag):
            yield ' '.join(elem.text_content().split())
    return extract


get_table_headings = tabular_node_extractor('th')
get_table_rows = tabular_node_extractor('td')


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
