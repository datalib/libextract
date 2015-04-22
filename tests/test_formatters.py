from pytest import fixture
from copy import deepcopy
from lxml import html
from libextract.formatters import table_list, table_json, chunks, chunk_gen


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



def test_chunk_gen():
    r = list(chunk_gen([1,2,3,4], 2))
    assert r == [[1, 2], [3, 4]]


def test_table_json(table):
    tjson = table_json(table)
    assert tjson == {
        'Name': ['Rodrigo', 'Eugene'],
        'Gender': ['male', 'male']
            }


def test_table_list(table):
    tlist = list(table_list(table))
    assert tlist == [['Name', 'Gender'],
                     ['Rodrigo', 'male'],
                     ['Eugene', 'male']]
