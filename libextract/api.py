from .core import parse_html, pipeline
from .tabular import STRATEGY as ARTICLE_TABLES
from .article import STRATEGY as ARTICLE_NODE


def extract(document, encoding='utf-8', strategy=ARTICLE_NODE):
    return pipeline(
        parse_html(document, encoding=encoding),
        strategy,
        )
