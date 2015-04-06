try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from chardet import detect
from lxml.html import parse, HTMLParser
from libextract.abstract import Finder


class HTMLFinder(Finder):
    nodes_with_text = '//*[not(self::script or self::style)]/\
                       text()[normalize-space()]/..'
    text_in_node = './/text()[normalize-space()]'

    filter_text = './/*[not(self::script or self::style or \
            self::figure or self::span or self::time)]/\
            text()[normalize-space()]'

    def __init__(self, document):
        self.document = document
        self.etree = parse(
            BytesIO(document),
            HTMLParser(encoding=detect(document)['encoding'],
                       remove_blank_text=True),
            )

    def xpath_finder(self):
        """
        Returns a function which returns the XPath
        query to a node when called with a node.
        """
        try:
            return self.etree.getroot().getroottree().getpath
        except AttributeError:
            return self.etree.getroottree().getpath

    def get_pairs(self):
        """
        Returns an iterable of parent-node to
        length of text in child node tuples.
        """
        xpath_to = self.xpath_finder()
        for node in self.etree.xpath(self.nodes_with_text):
            yield (
                    xpath_to(node).rsplit('/', 1)[0],
                    len(self.get_text(node)),
                )

    def get_text(self, node):
        """
        Get the text contained in a given node.
        """
        return ''.join(node.xpath(self.text_in_node))

    def get_final_text(self, selector):
        """
        Given a selector, selects the node and then
        returns the normalised text contained within
        that node.
        """
        return ' '.join(self.etree.xpath(selector)[0]
                                  .xpath(self.filter_text))
