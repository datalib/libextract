from lxml.html import HtmlElement
from statscounter import StatsCounter
from libextract.ors import articles, tabular
from .fixtures import foo_file


def test_articles(foo_file):
    results = articles(foo_file.read())

    assert isinstance(results, list)
    for node, text_length in results:
        assert isinstance(node, HtmlElement)
        assert isinstance(text_length, int)


def test_tabular(foo_file):
    results = tabular(foo_file.read())

    assert isinstance(results, list)
    for node, text_length in results:
        assert isinstance(node, HtmlElement)
        assert isinstance(text_length, StatsCounter)
