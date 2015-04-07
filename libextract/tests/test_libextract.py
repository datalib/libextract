import os
from unittest import TestCase
from libextract import extract

TESTS_DIR = os.path.dirname(__file__)

FOOS_FILENAME = os.path.join(TESTS_DIR, 'assets/full_of_foos.html')


class TestLibExtract(TestCase):
    def setUp(self):
        self.file = open(FOOS_FILENAME, 'r')
        self.text = self.file.read()

    def tearDown(self):
        self.file.close()

    def test_is_str(self):
        content = extract(self.text)
        self.assertTrue(isinstance(content, str))

    def test_str_is_foos(self, ):
        content = extract(self.text)
        foos = "foo. foo. foo. foo. foo. foo. foo. foo. foo."
        self.assertEqual(content, foos)
