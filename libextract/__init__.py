from libextract.html import STRATEGY
from libextract.coretools import pipeline


def extract(document):
    return pipeline(document, STRATEGY)
