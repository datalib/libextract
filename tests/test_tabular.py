import pytest
from statscounter import StatsCounter
from libextract.tabular import node_counter_argmax, select_score, filter_tags
from .fixtures import etree


def test_node_counter_argmax(etree):
    divs = etree.xpath('//body/article/div')[:3]
    rv = node_counter_argmax([
        (div, StatsCounter({'a': len(div) + idx}))
        for idx, div in enumerate(divs)
    ])
    assert list(rv) == [
        (divs[0], ('a', 0)),
        (divs[1], ('a', 1)),
        (divs[2], ('a', 2)),
    ]


def test_select_score():
    assert select_score((None, (None, 0))) == 0
    assert select_score([None, [None, 0]]) == 0


def test_filter_tags(etree):
    body = etree.find('//body')
    rv = filter_tags([(body, ('article', None))])

    assert list(rv) == [body]
    assert len(body) == 1
    assert [node.tag for node in body] == ['article']
