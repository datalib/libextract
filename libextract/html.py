from lxml.html import parse, HTMLParser
from .coretools import argmax, histogram


NODES_WITH_TEXT = '//*[not(self::script or self::style)]/text()/..'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'


def node_text_length(node):
    """
    Returns the length of the text contained within
    a given *node*.
    """
    words = len(node.text_content().split())
    return (words * 2) - 1


def get_etree(fileobj):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding='utf-8',
                            remove_blank_text=True))


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


STRATEGY = (get_etree, get_pairs, histogram, argmax, get_final_text)
