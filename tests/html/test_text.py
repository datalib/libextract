from unittest import TestCase
from tests.html import TestGetEtree
from libextract.html.text import get_node_length_pairs, node_text_length


class TestNodeTextLength(TestGetEtree):
    def runTest(self):
        res = self.etree.xpath('//body/article/div')
        for node in res:
            assert node_text_length(node) == 4
        assert res


class TestGetNodeLengthPairs(TestGetEtree):
    def runTest(self):
        u = list(get_node_length_pairs(self.etree))
        assert len(u) == 10

        for node, score in u:
            assert node.tag in {'article', 'body'}
            assert score in {4, 14}
