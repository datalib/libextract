"""
    libextract.core
    ~~~~~~~~~~~~~~~
    Implements the core utilities and functions in which
    libextract is built around.
"""


from lxml.html import parse, HTMLParser

__all__ = ['parse_html', 'pipeline']


def parse_html(fileobj, encoding):
    """
    Given a file object *fileobj*, get an ElementTree instance.
    The *encoding* is assumed to be utf8.
    """
    parser = HTMLParser(encoding=encoding, remove_blank_text=True)
    return parse(fileobj, parser)


def pipeline(data, funcs):
    """
    Pipes *functions* onto a given *data*, where the result
    of the previous function is fed to the next function.
    """
    for func in funcs:
        data = func(data)
    return data
