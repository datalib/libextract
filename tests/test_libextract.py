from pytest import fixture
from libextract import extract


def test_extract(foo_file):
    content = extract(foo_file.read())
    foos = "foo. foo. foo. foo. foo. foo. foo. foo. foo."

    assert isinstance(content, str)
    assert content == foos
