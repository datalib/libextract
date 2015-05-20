import pytest
from libextract.metrics import text_length, count_children
from .fixtures import etree


@pytest.fixture
def node(etree):
    return etree.find('//body/article/div[1]')


def test_text_length(node):
    assert text_length(node) == 4


def test_count_children(node):
    assert count_children(node) == {}
    assert count_children(node.getparent()) == {'div': 9}
