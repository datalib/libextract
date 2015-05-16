"""
    libextract.core
    ~~~~~~~~~~~~~~~
    Implements the core utilities and functions in which
    libextract is built around.
"""


from functools import partial
from lxml.html import parse, HTMLParser
from ._compat import BytesIO

__all__ = ['parse_html', 'pipeline']


def parse_html(document, encoding):
    """
    Given an X/HTML string *document*, get an ElementTree instance.
    The *encoding* is assumed to be utf8.
    """
    parser = HTMLParser(encoding=encoding, remove_blank_text=True)
    return parse(BytesIO(document), parser)


def pipeline(data, funcs):
    """
    Pipes *functions* onto a given *data*, where the result
    of the previous function is fed to the next function.
    """
    for func in funcs:
        data = func(data)
    return data
