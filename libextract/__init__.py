from .html import STRATEGY
from .coretools import pipeline


def extract(document):
    return pipeline(document, STRATEGY)
