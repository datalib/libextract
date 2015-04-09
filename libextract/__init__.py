try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from functools import partial
from chardet import detect
from .html import parse_html
from .coretools import pipeline
from .strategies import ARTICLE_TEXT


__all__ = ('extract',)


def extract(document, strategy=ARTICLE_TEXT):
    enc_etree = partial(parse_html,
                        encoding=detect(document)['encoding'])

    # TODO: This part is confusing
    return pipeline(BytesIO(document),
                    (enc_etree,) + strategy[1:])
