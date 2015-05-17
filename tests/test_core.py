from .fixtures import foo_file
from libextract.core import parse_html, pipeline


def test_parse_html(foo_file):
    etree = parse_html(foo_file, encoding='ascii')
    divs = etree.xpath('//body/article/div')

    for node in divs:
        assert node.tag == 'div'
        assert node.text == 'foo.'

    assert len(divs) == 9


def test_pipeline():
    functions = [
        lambda x: x + [1],
        lambda x: x + [2],
    ]
    assert pipeline([], functions) == [1, 2]
    assert pipeline([1], functions) == [1, 1, 2]
