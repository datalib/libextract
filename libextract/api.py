from ._compat import BytesIO
from .core import parse_html, pipeline
from .tabular import build_strategy as _tables
from .article import build_strategy as _nodes


ARTICLE_NODE = _nodes()
ARTICLE_TABLES = _tables()


def extract(document, encoding='utf-8', strategy=ARTICLE_NODE):
    if isinstance(document, bytes):
        document = BytesIO(document)
    return pipeline(
        parse_html(document, encoding=encoding),
        strategy,
        )
