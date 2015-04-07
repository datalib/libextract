import os
from unittest import TestCase
from tests import asset_path
from libextract import extract
from libextract.html import get_etree



FOOS_FILENAME = asset_path('full_of_foos.html')


class TestLibExtract(TestCase):
    def setUp(self):
        self.file = open(FOOS_FILENAME, 'r')
        self.content = extract(self.file.read())

    def tearDown(self):
        self.file.close()

    def test_is_str(self):
        self.assertTrue(isinstance(self.content, str))

    def test_str_is_foos(self):
        foos = "foo. foo. foo. foo. foo. foo. foo. foo. foo."
        self.assertEqual(self.content, foos)

    def test_get_etree_is_correct_article_etree(self):
        pass

