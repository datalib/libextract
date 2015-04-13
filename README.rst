Libextract: elegant text extraction
===================================

.. image:: https://travis-ci.org/libextract/libextract.svg?branch=master
    :target: https://travis-ci.org/libextract/libextract

::

        ___ __              __                  __
       / (_) /_  ___  _  __/ /__________ ______/ /_
      / / / __ \/ _ \| |/_/ __/ ___/ __ `/ ___/ __/
     / / / /_/ /  __/>  </ /_/ /  / /_/ / /__/ /_
    /_/_/_.___/\___/_/|_|\__/_/   \__,_/\___/\__/


Libextract is a statistical extraction library that works
on HTML and XML documents, written in Python and originating
from eatihit_. The philosophy and aim is to provide declaratively
composed, simple and pipelined functions for users to describe
their extraction algorithms.

Overview
--------

`libextract.extract(doc)`
    Extracts text (by default) from a given HT/XML string *doc*.
    What is extracted and how it is extracted can be configured
    using the *strategy* parameter, which accepts an iterable
    of functions to be piped to one another (the result of the
    previous is the argument of the next).

Usage
-----

Extracting the text from a wikipedia page:

.. code-block:: python

    from requests import get
    from libextract import extract

    r = get('http://en.wikipedia.org/wiki/Classifier_(linguistics)')
    text = extract(r.content)

Getting the node that (most likely) contains the text nodes that
contain the text of the article:

.. code-block:: python

    from libextract.strategies import ARTICLE_NODE

    node = extract(r.content, strategy=ARTICLE_NODE)

To serialize the node into JSON format:

.. code-block:: python

    >>> from libextract.formatters import node_json
    >>> node_json(node, depth=1)
    {'children': [...],
     'class': ['mw-content-ltr'],
     'id': ['mw-content-text'],
     'tag': 'div',
     'text': None,
     'xpath': '/html/body/div[3]/div[3]/div[4]'}

Using tabular extraction to get the nodes containing tabular data
present in the HT/XML document:

.. code-block:: python

    from libextract.strategies import TABULAR

    height_data = get("http://en.wikipedia.org/wiki/Human_height")
    tabs = list(extract(height_data.content, strategy=TABULAR))


To convert HT/XML element to python ``list``

.. code-block:: python

    >>> from libextract.formatters import table_json
    >>> table_json(tabs[0])
    [['Country/Region',
      'Average male height',
      'Average female height',
      'Stature ratio (male to female)',
      'Sample population / age range',
      ...]]


Viewing the table in your browser:

.. code-block:: python

    from lxml.html import open_in_browser
    open_in_browser(tabs[0])


.. _eatihit: http://rodricios.github.io/eatiht/
