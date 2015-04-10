from pytest import fixture
from copy import deepcopy
from lxml import etree
from libextract.formatters import node_json


@fixture
def elem():
    return etree.fromstring(
        '<html class="this those" id="that"><p>Hello World</p></html>'
    )


@fixture
def json():
    return {'children': None,
            'xpath': '/html',
            'class': ['this', 'those'],
            'text': None,
            'tag': 'html',
            'id': ['that']}


def test_node_json(elem, json):
    assert node_json(elem) == json


def test_depth(elem, json):
    json['children'] = [{
        'children': None,
        'xpath': '/html/p',
        'text': 'Hello World',
        'class': [],
        'id': [],
        'tag': 'p',
    }]
    expected = deepcopy(json)
    expected['children'][0]['children'] = []

    assert node_json(elem, depth=1) == json
    assert node_json(elem, depth=2) == expected
