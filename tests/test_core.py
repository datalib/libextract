from pytest import fixture
from libextract.core import pipeline, parse_html
from .fixtures import etree


@fixture
def pairs():
    return (('i', 5),
            ('h', 7),
            ('g', 20),
            ('i', 10))


def test_pipeline():
    pipe = [lambda x: x+2,
            lambda x: x+1,
            lambda x: x/2.0]
    assert pipeline(1, pipe) == 2
    assert pipeline(2, pipe) == 2.5


def test_parse_html(etree):
    divs = etree.xpath('//body/article/div')

    assert all(k.text == 'foo.' for k in divs)
    assert len(divs) == 9
