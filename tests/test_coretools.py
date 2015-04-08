from unittest import TestCase
from libextract.coretools import pipeline, histogram,\
        above_threshold, argmax


class PipelineTest(TestCase):
    def setUp(self):
        self.pipe = [lambda x: x+1,
                     lambda x: x+2,
                     lambda x: x/2.0]

    def runTest(self):
        self.assertEqual(pipeline(1, self.pipe), 2)
        self.assertEqual(pipeline(2, self.pipe), 2.5)


class HistogramTest(TestCase):
    def setUp(self):
        self.hist = histogram((('i', 10),
                               ('h', 20),
                               ('i', -5),
                               ('j', 50)))

    def runTest(self):
        self.assertEqual(self.hist['i'], 5)
        self.assertEqual(self.hist['h'], 20)
        self.assertEqual(self.hist['j'], 50)


class ArgmaxTest(HistogramTest):
    def runTest(self):
        self.assertEqual(argmax(self.hist), ('j', 50))
        self.hist.pop('j')
        self.assertEqual(argmax(self.hist), ('h', 20))


class AboveThresholdTest(TestCase):
    dataset = (('i', 8),
               ('h', 50),
               ('i', 10),
               ('k', 9))

    def setUp(self):
        self.func = above_threshold(9)

    def runTest(self):
        self.assertEqual(list(self.func(self.dataset)),
                         [('h', 50),
                          ('i', 10),
                          ('k', 9)])
