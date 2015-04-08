from lxml.html import parse, HTMLParser
from .coretools import argmax, histogram


NODES_WITH_TEXT = '//*[not(self::script or self::style)]/\
                     text()[normalize-space()]/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'


def _get_xpath_finder(etree):
    """Returns the lxml._ElementTree internal function
    that takes in an lxml.html.HtmlElement and returns
    its xpath"""
    try:
        xpath_finder = etree.getroot().getroottree().getpath
    except(AttributeError):
        xpath_finder = etree.getroottree().getpath



def node_text_length(node):
    """
    Returns the length of the text contained within
    a given *node*.
    """
    return len(' '.join(node.text_content().split()))


def get_etree(fileobj, encoding='utf-8'):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding=encoding,
                            remove_blank_text=True))

#TODO: the name "get_pairs" and the internal logic
#(particularly node_text_length) do not resonate well
def get_pairs(etree):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    for node in etree.xpath(NODES_WITH_TEXT):
        yield node.getparent(), node_text_length(node)


def get_final_text(pair):
    """
    Gets the text contained within the children node
    of a given node and text length *pair*, joined by
    a space.
    """
    node, _ = pair
    return ' '.join(node.xpath(FILTER_TEXT))
