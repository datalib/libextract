from lxml.html import parse, HTMLParser


def get_etree(fileobj, encoding='utf-8'):
    """
    Get an ElementTree instance from a given file object
    *fileobj*. The encoding is assumed to be utf8.
    """
    return parse(fileobj,
                 HTMLParser(encoding=encoding,
                            remove_blank_text=True))
