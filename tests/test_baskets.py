from tests.fixtures import element
from libextract.baskets import node_children_pairs_of, \
        parent_length_pairs_of


def test_node_children_pairs_of(element):
    func = node_children_pairs_of('/tag')
    u = list(func(element))
    assert u == [(element, {'nest': 2})]


def test_parent_length_pairs_of(element):
    func = parent_length_pairs_of('//nest')
    u = list(func(element))
    assert len(u) == 2

    for node, score in u:
        assert node.tag == 'tag'
        assert score in [2, 3]
