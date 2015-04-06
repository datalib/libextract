from libextract.abstract import extract_text as _extract_text
from libextract.html import HTMLFinder as _HTMLFinder


def extract(document):
    return _extract_text(_HTMLFinder(document))
