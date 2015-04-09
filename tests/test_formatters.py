from unittest import TestCase
from lxml import etree
from tests import asset_path
from libextract.formatters import node_json, tabular_json


FOOS_FILENAME = asset_path('full_of_foos.html')


class TestNodeJson(TestCase):
    def setUp(self):
        self.etree = etree.fromstring(
            '<html class="this those" id="that"><p>Hello World</p></html>'
            )

    def test_simple(self):
        assert node_json(self.etree) == {
            'xpath': '/html',
            'class': ['this', 'those'],
            'text': None,
            'tag': 'html',
            'id': ['that'],
        }

    def test_depth(self):
        assert node_json(self.etree, depth=1) == {
            'xpath': '/html',
            'text': None,
            'class': ['this', 'those'],
            'id': ['that'],
            'tag': 'html',
            'children': [{
                'xpath': '/html/p',
                'text': 'Hello World',
                'class': [],
                'id': [],
                'tag': 'p',
            }]
        }
