from functools import partial

from ._compat import BytesIO
from .core import parse_html, pipeline, select, measure, rank, finalise

def extract(document, encoding='utf-8', count=None):
    if isinstance(document, bytes):
        document = BytesIO(document)
    
    crank = partial(rank, count=count) if count else rank
    
    return pipeline(
        parse_html(document, encoding=encoding),
        (select, measure, crank, finalise)
        )
