from tests.html import TestGetEtree
from libextract.html.tabular import children_counter, \
        get_node_counter_pairs, node_counter_argmax, \
        sort_best_pairs


class TestChildrenCounter(TestGetEtree):
    def runTest(self):
        article = self.etree.xpath('//body/article')[0]
        counter = children_counter(article)

        assert len(counter) == 1
        assert counter['div'] == 9


class TestGetNodeCounterPairs(TestGetEtree):
    def setUp(self):
        TestGetEtree.setUp(self)
        self.pairs = get_node_counter_pairs(self.etree)

    def runTest(self):
        u = {elem.tag: counter for elem, counter in self.pairs}
        u.pop('head')
        assert u == {
            'article': {'div': 9},
            'body': {'article': 1, 'footer': 1},
            'html': {'body': 1, 'head': 1},
            }


class TestSortBestPairs(TestGetNodeCounterPairs):
    def runTest(self):
        article = self.etree.xpath('//body/article')[0]
        u = sort_best_pairs(node_counter_argmax(self.pairs), limit=1)
        assert u == [
            (article, [('div', 9)])
            ]
