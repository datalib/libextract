from .fixtures import foo_file
from libextract.api import extract


def test_extract(foo_file):
    r = extract(foo_file)
    u = [(node.tag, score) for node, score in r]
    assert u == [
        ('article', 36),
        ('body', 14),
    ]
