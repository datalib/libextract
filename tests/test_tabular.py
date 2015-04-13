from collections import Counter
from tests.fixtures import element, etree
from libextract.tabular import node_counter_argmax, select_score, weighted_score, \
        get_top_pairs, filter_tags


def test_node_counter_argmax(element):
    data = [
        (element, Counter(a=1, b=3)),
        (element, Counter(a=2, b=1)),
    ]
    assert list(node_counter_argmax(data)) == [
        (element, ('b', 3)),
        (element, ('a', 2)),
    ]


def test_select_score():
    assert select_score(('node', ('tag', 2))) == 2


def test_weighted_score(element):
    f = weighted_score(favours={'article'}, k=2)
    assert f((element, ('tag', 2))) == 2

    g = weighted_score(favours={'tag'})
    assert g((element, ('tag', 2))) == 3


def test_get_top_pairs():
    f = get_top_pairs(2, int)
    assert f([1,2,3,4]) == [4,3]


def test_filter_tags(etree):
    body = etree.xpath('//body')[0]
    assert list(filter_tags([(body, ('article', 0))])) == [body]

    for child in body:
        assert child.tag == 'article'
