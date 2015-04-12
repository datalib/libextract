"""
    libextract
    ~~~~~~~~~~

    Beautfully simple text extraction using simple,
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
from libextract.coretools import pipeline, parse_html
from libextract.strategies import ARTICLE_TEXT


__all__ = ('extract',)


def extract(document, encoding=None, strategy=ARTICLE_TEXT):
    """
    Given an X/HTML string *document*, process the
    document using the given *strategy* and returns
    the result.
    """
    enc_etree = partial(parse_html,
                        encoding=encoding or detect(document)['encoding'])

    return pipeline(BytesIO(document),
                    (enc_etree,) + strategy[1:])
