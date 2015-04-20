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

from itertools import islice
from functools import partial
from chardet import detect
from ..coretools import parse_html
from ..strategies import ARTICLE_TEXT


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
    #data = (data,)
    for func in funcs:
        print("pipeline.data,func;pre-yield", data, func)
        data = func(data)
        print("pipeline.data,func;post-yield", data, func, '\n')
    return data
