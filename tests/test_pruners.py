from pytest import fixture
from collections import Counter

from libextract.pruners import prune_by_child_count, prune_by_text_length


@fixture
def pairs(etree):
    return prune_by_child_count(etree)


def test_prune_by_child_count(pairs):
    u = {elem.tag: counter for elem, counter in pairs}
    u.pop('head')
    print(u)
    assert u == {
        'article': {'div': 9},
        'body': {'article': 1, 'footer': 1},
        'html': {'body': 1, 'head': 1},
        'footer': Counter(),
        'div': Counter()
        }


def test_prune_by_text_length(etree):
    u = list(prune_by_text_length(etree))
    assert len(u) == 10

    for node, score in u:
        assert node.tag in {'article', 'body'}
        assert score in {4, 14}
