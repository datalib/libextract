from ._compat import BytesIO
from .core import parse_html, pipeline
from .tabular import TabularExtractor
from .article import ArticleExtractor


ARTICLE_NODE = ArticleExtractor().compile_pipeline()
ARTICLE_TABLES = TabularExtractor().compile_pipeline()


def extract(document, encoding='utf-8', strategy=ARTICLE_NODE):
    if isinstance(document, bytes):
        document = BytesIO(document)
    return pipeline(
        parse_html(document, encoding=encoding),
        strategy,
        )
