from unittest import TestCase
from tests.html.test_commons import TestGetEtree
from libextract.html.text import get_pairs, node_text_length


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
