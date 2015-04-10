from copy import deepcopy
from unittest import TestCase
from lxml import etree
from libextract.formatters import node_json


class TestNodeJson(TestCase):
    def setUp(self):
        self.etree = etree.fromstring(
            '<html class="this those" id="that"><p>Hello World</p></html>'
            )
        self.expected_json = {
            'children': None,
            'xpath': '/html',
            'class': ['this', 'those'],
            'text': None,
            'tag': 'html',
            'id': ['that'],
        }

    def test_simple(self):
        assert node_json(self.etree) == self.expected_json

    def test_depth(self):
        self.expected_json['children'] = [{
            'children': None,
            'xpath': '/html/p',
            'text': 'Hello World',
            'class': [],
            'id': [],
            'tag': 'p',
        }]
        expected = deepcopy(self.expected_json)
        expected['children'][0]['children'] = []

        assert node_json(self.etree, depth=1) == self.expected_json
        assert node_json(self.etree, depth=2) == expected
