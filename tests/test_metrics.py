from tests.fixtures import element
from libextract.metrics import text_length, count_children


def test_text_length(element):
    assert text_length(element) == 0
    assert [text_length(k) for k in element] == [2, 3]


def test_count_children(element):
    assert count_children(element) == {'nest': 2}
    assert count_children(element[0]) == {}
