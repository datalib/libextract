"""
    libextract
    ~~~~~~~~~~

    Beautfully simple data extraction using simple,
    composable pipelined functions.

    :copyright: (c) 2015 Libextract
    :license: MIT, see LICENSE for details.
"""

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from functools import partial
from chardet import detect
from lxml.html import parse, HTMLParser


def parse_html(fileobj, encoding='utf-8'):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding=encoding,
                            remove_blank_text=True))


def extract(document, encoding=None):
    """
    """
    enc_etree = partial(parse_html,
                        encoding=encoding or detect(document)['encoding'])

    return enc_etree(BytesIO(document))


def pipeline(data, funcs):
    """
    Pipes *functions* onto a given *data*, where the result
    of the previous function is fed to the next function.
    """
    for func in funcs:
        data = func(data)
    return data
