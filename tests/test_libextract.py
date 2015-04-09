import os
from unittest import TestCase
from tests import asset_path
from libextract import extract


FOOS_FILENAME = asset_path('full_of_foos.html')


class TestLibExtract(TestCase):
    def setUp(self):
        with open(FOOS_FILENAME, 'rb') as fp:
            self.content = extract(fp.read())

    def test_is_str(self):
        assert isinstance(self.content, str)

    def test_str_is_foos(self):
        foos = "foo. foo. foo. foo. foo. foo. foo. foo. foo."
        assert self.content == foos
