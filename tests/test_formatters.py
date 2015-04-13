from pytest import fixture
from copy import deepcopy
from lxml import html
from libextract.formatters import node_json, table_list, table_json, chunks


@fixture
def elem():
    return html.fromstring(
        '<html class="this those" id="that"><body>Hello World</body></html>'
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
        'xpath': '/html/body',
        'text': 'Hello World',
        'class': [],
        'id': [],
        'tag': 'body',
    }
    json['children'] = [child]
    assert node_json(elem, depth=1) == json

    child['children'] = []
    assert node_json(elem, depth=2) == json


def test_chunks():
    r = list(chunks([1,2,3,4], 2))
    assert r == [[1, 2], [3, 4]]


def test_table_json(table):
<<<<<<< HEAD
    tjson = table_json(table)
    assert tjson == {
        'Name': ['Rodrigo', 'Eugene'],
        'Gender': ['male', 'male']
            }


def test_table_list(table):
    tlist = list(table_list(table))
    assert tlist == [['Name', 'Gender'],
=======
    table = table_json(table)
    assert table == [['Name', 'Gender'],
>>>>>>> dc2fa31fd91da1c0384243c3cb2a7dd87f11ca69
                     ['Rodrigo', 'male'],
                     ['Eugene', 'male']]
