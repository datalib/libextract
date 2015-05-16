try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest

from .generators import iters
from .xpaths import FILTER_TEXT
from statscounter import stats

UNLIMITED = float('NaN')


def chunks(iterable, size):
    args = [iter(iterable)] * size
    for row in zip_longest(*args, fillvalue=None):
        yield list(row)


@iters('th')
def table_headings(node):
    return " ".join(node.text_content().split())


@iters('td')
def table_data(node):
    return " ".join(node.text_content().split())


@iters('td')
def table_data_count(node):
    return 1


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


def table_list(node):
    """
    Given a table *HtmlElement* (ie. <table>), return
    a list of lists, where the first list contains the
    table headings, and the subsequent lists contain
    rows of data.
    """
    headings = list(table_headings(node))
    rows = table_data(node)
    table = [headings]
    table.extend(chunks(rows, len(headings)))
    return table


def table_json(node):
    """
    Given a table *node* (ie. <table>), return a dictionary
    of key-value pairs, where the key is the heading and the
    value is a list of rows.
    """
    headings = list(table_headings(node))

    if not headings:
        return None

    rows = list(chunks(table_data(node), len(headings)))
    return {heading: [row[col] for row in rows]
            for col, heading in enumerate(headings)}


def to_dict(node):
    table = table_json(node)
    if not table:
        mode = stats.mode(table_data_count(node))
        rows = [tds for tds in (node) if len(tds) == mode]

        table = {str(col): [' '.join(row[col].text_content().split())
                            for row in rows]
                 for col in range(mode)}
    return table
