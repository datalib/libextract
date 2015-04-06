"""eatiht algo"""

import collections

import re

import chardet

import urllib2

import cookielib



try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from lxml import html

from lxml.html.clean import clean_html


TEXT_XPATH = '//*[not(self::script or self::style)]/\
                    text()[normalize-space()]/..'

NORM_TEXT_XPATH = './/text()[normalize-space()]'

FILTER_NORM_TEXT_XPATH = './/*[not(self::script or self::style or \
                  self::figure or self::span or self::time)]/\
                  text()[normalize-space()]'

def _etree_from_string(string):
    """Detect encoding and parse string into lxml's element tree"""

    encoding = chardet.detect(string)['encoding']

    parsed_html = html.parse(BytesIO(string),
                             html.HTMLParser(encoding=encoding,
                                             remove_blank_text=True))

    return parsed_html


def _etree_from_url(url):
    """Given URL, construct and return an element tree.
    """
    handler = (urllib2.HTTPSHandler
               if url.lower().startswith('https')
               else urllib2.HTTPHandler)

    cookiejar = cookielib.CookieJar()

    opener = urllib2.build_opener(handler)

    opener.add_handler(urllib2.HTTPCookieProcessor(cookiejar))

    resp = opener.open(url)

    try:
        content = resp.read()
    finally:
        resp.close()

    return _etree_from_string(content)

def _get_path_textlen_pairs(etree, xpath_to_text=TEXT_XPATH):
    """
    Given a url and xpath, this function will download, parse, then
    iterate though queried text-nodes. From the resulting text-nodes,
    extract a list of (text, exact-xpath) tuples.
    """

    try:
        xpath_finder = etree.getroot().getroottree().getpath

    except(AttributeError):
        xpath_finder = etree.getroottree().getpath


    nodes_with_text = etree.xpath(xpath_to_text)

    xpath_textlen_pairs = []

    for node in nodes_with_text:
        #for wikipedia pages ("[12]")
        text = ''.join(node.xpath(NORM_TEXT_XPATH))

        #get path of parent node by rsplit'ing
        #the rsplit'ing logic was moved from get_xpath_frequencydistribution
        xpath_textlen_pairs.append((xpath_finder(node).rsplit('/', 1)[0],
                                    len(text)))

    return xpath_textlen_pairs


def _get_path_textlen_fdistribution(xpath_textlen_pairs):
    """Return Counter object with xpaths-to-textlength
    frequency distribution"""
    histogram = collections.Counter()

    for path, count in xpath_textlen_pairs:
        histogram[path] += count

    return histogram


def _get_content_etree(etree):
    """ Get list of text-nodes, text-length pairs, then get their parents.
    Then we make a histogram and get the highest scoring one.

    We use xpaths to determine which node to extract.
    """

    pairs = _get_path_textlen_pairs(etree)

    histogram = _get_path_textlen_fdistribution(pairs)

    path_to_text = histogram.most_common(1)[0][0]

    content_etree = etree.xpath(path_to_text)

    #there should only be one path
    assert len(content_etree) is 1

    return content_etree[0]


def extract(url):
    """Eatiht algo."""

    etree = _etree_from_url(url)

    content_etree = _get_content_etree(etree)

    content = ' '.join(content_etree.xpath(FILTER_NORM_TEXT_XPATH))

    return content
