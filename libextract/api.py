from .core import parse_html, pipeline
from .metrics import text_length
from .procs import select, rank_with, get_largest
from .tabular import STRATEGY as ARTICLE_TABLES
from .xpaths import TEXT


ARTICLE_NODE = (
    select(TEXT),
    rank_with(text_length),
    get_largest(5),
)


def extract(document, encoding='utf-8', strategy=ARTICLE_NODE):
    return pipeline(
        parse_html(document, encoding=encoding),
        strategy,
        )
