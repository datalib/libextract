from unittest import TestCase
from libextract.coretools import pipeline, histogram,\
        above_threshold, argmax


class TestCoretools(TestCase):
    data = (
        ('i', 5),
        ('h', 7),
        ('g', 20),
        ('i', 10),
    )

    def test_pipeline(self):
        pipe = [lambda x: x+2,
                lambda x: x+1,
                lambda x: x/2.0]
        assert pipeline(1, pipe) == 2
        assert pipeline(2, pipe) == 2.5

    def test_histogram(self):
        hist = histogram(self.data)
        assert hist['i'] == 15
        assert hist['g'] == 20

    def test_above_threshold(self):
        func = above_threshold(7)
        assert list(func(self.data)) == [
                ('h', 7),
                ('g', 20),
                ('i', 10)
                ]

    def test_argmax(self):
        hist = histogram(self.data)
        assert argmax(hist) == ('g', 20)
