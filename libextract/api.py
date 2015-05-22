from ._compat import BytesIO
from .core import parse_html, pipeline, select, measure, rank, finalise

def extract(document, encoding='utf-8'):
    if isinstance(document, bytes):
        document = BytesIO(document)
    return pipeline(
        parse_html(document, encoding=encoding),
        (select, measure, rank, finalise)
        )
