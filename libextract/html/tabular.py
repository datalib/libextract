from .coretools import Counter


SELECT_ALL = '//*'


#TODO: Consolidate get_pairs functions
#TODO: Converge on get_*, filter_*
#TODO: Better yet, decide on "meta/pipelining language"

def _get_xpath_finder(etree):
    """Returns the lxml._ElementTree internal function
    that takes in an lxml.html.HtmlElement and returns
    its xpath"""
    try:
        xpath_finder = etree.getroot().getroottree().getpath
    except(AttributeError):
        xpath_finder = etree.getroottree().getpath


def node_children_counter(node):
    """
    Returns the a collections.Counter object measuring the
    frequenies of the children nodes (by tag name) contained
    within a given *node*.
    """
    return Counter([child.tag for child in node])


def get_node_children_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to child node frequencies (collections.Counter) length pairs.
    """
    for node in etree.xpath(SELECT_ALL):
        nc_counter = node_children_counter(node)
        if nc_counter:
            yield node, nc_counter


def filter_node_children_pairs(pairs, top=1):
    for (node, children) in pairs:
        yield first, children.most_common(top)
