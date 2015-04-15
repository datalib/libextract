from libextract.baskets import node_children_pairs, \
        parent_length_pairs
from .fixtures import element


def test_node_children_pairs(element):
    u = list(node_children_pairs(element))
    assert u == [(element, {'nest': 2})]


def test_parent_length_pairs(element):
    u = list(parent_length_pairs(element))
    assert len(u) == 2

    for node, score in u:
        assert node.tag == 'tag'
        assert score in [2, 3]
