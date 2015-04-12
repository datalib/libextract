from pytest import fixture
from lxml import etree
from libextract.pruners import subnode_count_pruner
from libextract.html.tabular import node_counter_argmax, \
        sort_best_pairs, weighted_score, filter_tags


@fixture
def pairs(etree):
    return subnode_count_pruner(etree)


@fixture
def article(etree):
    return etree.xpath('//body/article')[0]


@fixture
def sorted_pairs(pairs):
    return sort_best_pairs(node_counter_argmax(pairs),
                           top=1)


def test_sort_best_pairs(sorted_pairs, article):
    assert sorted_pairs == [
        (article, ('div', 9))
        ]


def test_weighted_score():
    elem = etree.fromstring('<table></table>')

    assert weighted_score((elem, ('a', 10)), k=10) == 100
    assert weighted_score((elem, ('a', 1)),
                          favours={'article'}) == 1


def test_filter_tags(sorted_pairs, article):
    u = list(filter_tags(sorted_pairs))
    assert u == [article]

    for child in article:
        assert child.tag == 'div'
