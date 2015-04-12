from pytest import fixture
from copy import deepcopy
from lxml import etree
from lxml import html
from libextract.formatters import node_json, get_table_as_header_rows_list


@fixture
def elem():
    return etree.fromstring(
        '<html class="this those" id="that"><p>Hello World</p></html>'
    )

@fixture
def table():
    return html.fromstring(
        '<table>\
            <thead>\
                <tr>\
                    <th>Name</th>\
                    <th>Gender</th>\
                </tr>\
            </thead>\
            <tbody>\
                <tr>\
                    <td>Rodrigo</td>\
                    <td>male</td>\
                </tr>\
                <tr>\
                    <td>Eugene</td>\
                    <td>male</td>\
                </tr>\
            </tbody>\
        </table>'
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


def test_get_table_as_header_rows_list(table):
    lists = get_table_as_header_rows_list(table)
    assert lists[0] == ['Name', 'Gender']
    assert lists[1] == ['Rodrigo', 'male']
    assert lists[2] == ['Eugene', 'male']
