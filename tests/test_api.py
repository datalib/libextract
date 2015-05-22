from .fixtures import foo_file, etree
from libextract.api import extract, pipeline, select, measure, rank, finalise
from statscounter import StatsCounter

def test_extract(foo_file):
    r = extract(foo_file)
    u = [node.tag for node in r]
    assert u == [
        'article',
        'body',
    ]


def test_extract_tabular(foo_file):
    r = list(extract(foo_file))
    u = [node.tag for node in r]
    assert u == [
        'article',
        'body',
    ]
    for node in r[0]:
        assert node.tag == 'div'


def test_pipeline(etree):
    funcs = (select, measure, rank, finalise)
    assert list(pipeline(etree, funcs)) == [etree.xpath('//article')[0],
                                            etree.xpath('//body')[0]]


def test_select(etree):
    assert select(etree) == etree.xpath('//body//*/..')


def test_measure(etree):
    rv = measure(etree.xpath('//div/..'))
    uv = [(node.tag, metric) for node, metric in rv]

    assert uv == [('article', StatsCounter(['div']*9))] 


def test_rank(etree):
    k = measure(etree.xpath('//body//*/..'))
    rv = rank(k)

    assert list(rv)[0] ==  (etree.xpath('//article')[0],
                            StatsCounter(['div']*9))


def test_finalise(etree):
    datum = [('k', 1), ('b', 2)]
    assert list(finalise(datum)) == ['k','b']