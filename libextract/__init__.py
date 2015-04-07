try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from functools import partial
from chardet import detect
from .html import get_etree
from .coretools import pipeline
from .strategies import ARTICLE_TEXT

__all__ = ('extract',)


def get_stream(document):
    t = BytesIO(document)
    return t, detect(document)['encoding']


def extract(document, strategy=ARTICLE_TEXT):
    enc_etree = partial(get_etree,
                        encoding=detect(document)['encoding'])

    #TODO: This part is confusing
    return pipeline(BytesIO(document),
                    (enc_etree,) + strategy[1:])
