libextract
==========

**libextract** is a library for extracting text out of HT/XML
documents using a statistical, functionally pure approach. It
originated from the eatihit_ repository.

From a very high level persepective, the algorithm can be
reduced to around 4 steps:

- Find the text nodes in the page.
- Make a histogram of the their parents and text length.
- The highest scoring parent node is selected.
- The text in the highest scoring one is joined in a string
  and returned as the result of the extraction.

At the lowest level, **libextract** is just a pipelining
library. It provides composable, small functions that can
be piped together to process the HT/XML document.

.. _eatihit: http://rodricios.github.io/eatiht/

Usage
-----

.. code-block:: python

    from requests import get
    from libextract import extract
    from libextract.strategies import ARTICLE_NODE

    r = get('http://en.wikipedia.org/wiki/Classifier_(linguistics)')
    text = extract(r.content)

    # To get the HT/XML node:
    node = extract(r.content, strategy=ARTICLE_NODE)

    # Tabular data extraction

    from libextract.strategies import TABULAR
    reddit = get("http://reddit.com")
    tabs = extract(reddit.content, strategy=TABULAR))
