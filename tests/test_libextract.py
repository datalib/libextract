from pytest import fixture
from libextract import extract


FOOS = "foo. foo. foo. foo. foo. foo. foo. foo. foo."


def test_extract(foo_file):
    content = extract(foo_file.read())

    assert isinstance(content, str)
    assert content == FOOS


def test_extract_encoding(foo_file):
    content = extract(foo_file.read(), encoding='ascii')
    assert content == FOOS
