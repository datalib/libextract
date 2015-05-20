import pytest
from libextract.article import parent_score_pairs, ArticleExtractor
from .fixtures import etree


def test_parent_score_pairs(etree):
    data = [(node, 0) for node in etree.iter('div')]

    for node, score in parent_score_pairs(data):
        assert node.tag == 'article'
        assert score == 0

    assert len(data) == 9


class TestArticleExtractor:
    @pytest.fixture(autouse=True)
    def inject_etree(self, etree):
        self.etree = etree
        self.article = etree.find('//body/article')
        self.extractor = ArticleExtractor()

    def test_measure(self):
        rv = self.extractor.measure(self.article)
        assert list(rv) == [(self.article, 4)] * len(self.article)

    def test_rank(self):
        rv = self.extractor.measure(self.article)
        assert self.extractor.rank(rv) == [(
            self.article,
            4 * len(self.article),
        )]
