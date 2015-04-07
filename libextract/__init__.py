try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from functools import partial
from chardet import detect
from .html import STRATEGY, get_etree
from .coretools import pipeline


__all__ = ('extract',)


def get_stream(document):
    t = BytesIO(document)
    return t, detect(document)['encoding']


def extract(document):
    enc_etree = partial(get_etree,
                        encoding=detect(document)['encoding'])
    return pipeline(BytesIO(document),
                    (enc_etree,) + STRATEGY[1:])
