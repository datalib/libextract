from pytest import fixture
from libextract.core import pipeline
from libextract.extractor import Extractor
from .fixtures import etree


class MockedExtractor(Extractor):
    xpath = '/html'
    metric = staticmethod(lambda k: len(k.tag))


class TestExtractor:
    @fixture(autouse=True)
    def inject_extractor(self):
        self.extractor = MockedExtractor()

    def test_pipeline(self, etree):
        funcs = self.extractor.compile_pipeline()
        assert list(pipeline(etree, funcs)) == etree.xpath('/html')

    def test_select(self, etree):
        assert self.extractor.select(etree) == etree.xpath('/html')

    def test_measure(self, etree):
        rv = self.extractor.measure(etree.xpath('//*/div'))
        uv = [(node.tag, metric) for node, metric in rv]

        assert uv == [('div', 3)] * 9

    def test_rank(self, etree):
        k = [(node.tag, i) for i, node in enumerate(etree.xpath('//*/div'))]
        rv = self.extractor.rank(k)

        assert list(rv) == [
            ('div', i) for i in [8,7,6,5,4]
        ]

    def test_finalise(self, etree):
        datum = [('k', 1), ('b', 2)]
        assert list(self.extractor.finalise(datum)) == ['k','b']
