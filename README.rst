libextract
==========

**libextract** is a library for extracting text out of HT/XML
documents using a statistical, functionally pure approach. It
originated from the eatiht_ repository. Usage example:

.. _eatiht: https://github.com/rodricios/eatiht

.. code-block:: python

    from requests import get
    from libextract import extract

    r = get('http://en.wikipedia.org/wiki/Classifier_(linguistics)')
    text = extract(r.content)

From a very high level persepective, the algorithm is very
simple:

- It gets the text nodes in the page.
- A histogram of the text nodes is built up.
- The highest scoring parent node (one with most child text
  nodes) is selected.
- The text in the highest scoring one is joined in a string
  and returned as the result of the extraction.

.. _eatihit: http://rodricios.github.io/eatiht/
