import os
from unittest import TestCase

from .. import extract

THIS_FILE = os.path.dirname(__file__)

FOOS_FILENAME = os.path.join(THIS_FILE, 'assets/full_of_foos.html')

# Testdata file declarations
RE_SPLIT_VARIOUS_ENDINGS_FILENAME = os.path.join(THIS_FILE,'assets/regex_various_endings.html')

RE_SPLIT_DOT_ENDINGS_FILENAME = os.path.join(THIS_FILE,'assets/regex_dot_endings.html')


class TestLibExtract(TestCase):
    def setUp(self):
        self.file = open(FOOS_FILENAME, 'r')
        self.text = self.file.read()

    def tearDown(self):
        self.file.close()

    def test_is_str(self):
        content = extract(self.text)

        print(content)

        self.assertTrue(isinstance(content, str))

    def test_str_is_foos(self, ):
        content = extract(self.text)

        foos = "foo. foo. foo. foo. foo. foo. foo. foo. foo."

        self.assertEqual(content, foos)
