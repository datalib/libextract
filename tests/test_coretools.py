from pytest import fixture
from libextract.coretools import pipeline, histogram, argmax


@fixture
def pairs():
    return (('i', 5),
            ('h', 7),
            ('g', 20),
            ('i', 10))



def test_pipeline():
    pipe = [lambda x: x+2,
            lambda x: x+1,
            lambda x: x/2.0]
    assert pipeline(1, pipe) == 2
    assert pipeline(2, pipe) == 2.5


def test_histogram(pairs):
    hist = histogram(pairs)
    assert hist['i'] == 15
    assert hist['g'] == 20


def test_argmax(pairs):
    hist = histogram(pairs)
    assert argmax(hist) == ('g', 20)
