try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest

from .generators import iters
from .xpaths import FILTER_TEXT
from statscounter import stats

UNLIMITED = float('NaN')


def chunks(iterable, size):
    """
    Yield successive chunks of *size* from a given
    *iterable*, filling the unfilled chunks with
    None.
    """
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]


def chunk_gen(iterable, size):
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
    table.extend(chunk_gen(rows, len(headings)))
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

    rows = list(chunk_gen(table_data(node), len(headings)))
    return {heading: [row[col] for row in rows]
            for col, heading in enumerate(headings)}


def convert_table(node):
    table = table_json(node)
    if not table:
        mode = stats.mode(table_data_count(node))
        rows = [tds for tds in (node) if len(tds) == mode]

        table = {str(col): [' '.join(row[col].text_content().split())
                            for row in rows]
                 for col in range(mode)}
    return table
