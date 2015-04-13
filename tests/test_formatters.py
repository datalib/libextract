from pytest import fixture
from copy import deepcopy
from lxml import etree
from lxml import html
from libextract.formatters import node_json, table_json


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
    child = {
        'children': None,
        'xpath': '/html/p',
        'text': 'Hello World',
        'class': [],
        'id': [],
        'tag': 'p',
    }
    json['children'] = [child]
    assert node_json(elem, depth=1) == json

    child['children'] = []
    assert node_json(elem, depth=2) == json


def test_table_json(table):
    table = table_json(table)
    assert table == [['Name', 'Gender'],
                     ['Rodrigo', 'male'],
                     ['Eugene', 'male']]
