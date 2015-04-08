from unittest import TestCase
from tests import asset_path
from libextract.html import get_etree, get_pairs, node_text_length


FOO_ASSET = asset_path('full_of_foos.html')


class TestGetEtree(TestCase):
    def setUp(self):
        with open(FOO_ASSET, 'rb') as fp:
            self.etree = get_etree(fp)

    def runTest(self):
        divs = self.etree.xpath('//body/article/div')
        assert all(k.text == 'foo.' for k in divs)
        assert len(divs) == 9


class TestNodeTextLength(TestGetEtree):
    def runTest(self):
        res = self.etree.xpath('//body/article/div')
        for node in res:
            assert node_text_length(node) == 4
        assert res


class TestGetPairs(TestGetEtree):
    def runTest(self):
        u = list(get_pairs(self.etree))
        assert len(u) == 10

        for node, score in u:
            assert node.tag in {'article', 'body'}
            assert score in {4, 14}
