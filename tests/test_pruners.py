from pytest import fixture

from libextract.pruners import subnode_count_pruner, subnode_textlen_pruner


@fixture
def pairs(etree):
    return subnode_count_pruner(etree)


def test_subnode_count_pruner(pairs):
    u = {elem.tag: counter for elem, counter in pairs}
    u.pop('head')
    print(u)
    assert u == {
        'article': {'div': 9},
        'body': {'article': 1, 'footer': 1},
        'html': {'body': 1, 'head': 1},
        'footer': {'':0},
        'div': {'':0},
        }


def test_subnode_textlength_pruner(etree):
    u = list(subnode_textlen_pruner(etree))
    assert len(u) == 10

    for node, score in u:
        assert node.tag in {'article', 'body'}
        assert score in {4, 14}
