try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from .html import STRATEGY
from .coretools import pipeline


__all__ = ('extract',)


def extract(document):
    return pipeline(document, (BytesIO,) + STRATEGY)
