from .fixtures import foo_file
from libextract.api import extract


def test_extract(foo_file):
    r = extract(foo_file)
    assert len(r) == 2

    node, score = r[0]

    assert node.tag == 'article'
    assert score == 4 * 9
