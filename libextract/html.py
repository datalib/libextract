try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from chardet import detect
from lxml.html import parse, HTMLParser
from libextract.coretools import highest_scoring, memoized


NODES_WITH_TEXT = '//*[not(self::script or self::style)]/text()/..'
TEXT_IN_NODE = './/text()[normalize-space()]'

FILTER_TEXT = './/*[not(self::script or self::style or \
        self::figure or self::span or self::time)]/\
        text()[normalize-space()]'


def get_xpath_finder(etree):
    if hasattr(etree, 'getroot'):
        etree = etree.getroot()
    return etree.getroottree().getpath


def parent_finder(etree):
    xpath_for = get_xpath_finder(etree)
    getter = memoized(lambda k: etree.xpath(k)[0])

    def finder(node):
        parent = xpath_for(node).rsplit('/', 1)[0]
        return getter(parent)

    return finder


def node_text_length(node):
    return len(''.join(node.xpath(TEXT_IN_NODE)))


def get_etree(document):
    return parse(BytesIO(document),
                 HTMLParser(encoding=detect(document)['encoding'],
                            remove_blank_text=True))


def get_pairs(etree):
    parent_of = parent_finder(etree)
    for node in etree.xpath(NODES_WITH_TEXT):
        yield parent_of(node), node_text_length(node)


def get_final_text(node):
    return ' '.join(node.xpath(FILTER_TEXT))


STRATEGY = (get_etree, get_pairs, highest_scoring, get_final_text)
