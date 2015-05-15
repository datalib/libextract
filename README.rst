Libextract: simple data extraction
===================================

.. image:: https://travis-ci.org/datalib/libextract.svg?branch=master
    :target: https://travis-ci.org/datalib/libextract

::

        ___ __              __                  __
       / (_) /_  ___  _  __/ /__________ ______/ /_
      / / / __ \/ _ \| |/_/ __/ ___/ __ `/ ___/ __/
     / / / /_/ /  __/>  </ /_/ /  / /_/ / /__/ /_
    /_/_/_.___/\___/_/|_|\__/_/   \__,_/\___/\__/


Libextract is a `statistics-enabled
<https://github.com/datalib/StatsCounter>`_
extraction library that works on HTML and XML documents, written in Python
and originating from `eatiht
<http://rodricios.github.io/eatiht/>`_.


Overview
--------

Libextract provides two extractors out-of-the-box: ``api.articles`` and ``api.tabular``


`libextract.api.articles(document, encoding='utf-8', count=5)`

    Given an html document, and optionally the encoding
    and the number of predictions (count) to return
    (in descending rank), ``articles`` returns a list of HTML-nodes
    likely containing the articles of text of a given website.

    The extraction algorithm is based of text length.
    Refer to rodricios.github.io/eatiht for an in-depth
    explanation.

`libextract.api.tabular(document, encoding='utf-8', count=5)`

    Given an html *document*, and optionally the *encoding*,
    and the number of predictions (*count*) to return
    (in descending rank) *tabular* returns a list of HTML
    nodes likely containing "tabular" data (ie. table,
    and table-like elements).
    

Installation
------------

::

    pip install libextract

Usage
-----

Extracting text-nodes from a wikipedia page:

.. code-block:: python

    from requests import get
    from libextract.api import articles

    r = get('http://en.wikipedia.org/wiki/Information_extraction')
    textnodes = articles(r.content)

Libextract uses Python's de facto HT/XML processing library, `lxml
<http://lxml.de/index.html>`_. 

The predictions returned by both ``api.articles`` and ``api.tabular`` are 
`lxml HtmlElement
<http://lxml.de/lxmlhtml.html>`_ objects (along with the associated
*metric* used to rank each prediction). 

Therefore, you can access lxml's methods for post-processing.

.. code-block:: python

    >> print(textnodes[0][0].text_content())
    Information extraction (IE) is the task of automatically extracting structured information...
    

Tabular-data extraction is just as easy.

.. code-block:: python

    from libextract.api import tabular

    height_data = get("http://en.wikipedia.org/wiki/Human_height")
    tabs = tabular(height_data.content)

To convert HT/XML element to python ``dict`` (and, you know, 
`use it with Pandas and stuff
<https://github.com/datalib/libextract.ipynb/blob/master/libextract%20visualizing%20open%20secrets.ipynb>`_):

.. code-block:: python

    >>> from libextract import clean
    >>> clean.to_dict(tabs[0])
    {'Entity': ['Monaco',
      'Macau',
      'Japan',
      'Singapore',
      'San Marino',
      ...}

Dependencies
~~~~~~~~~~~~

::

    lxml
    statscounter
    
Disclaimer
~~~~~~~~~~

This project is still in its infancy; and advice and suggestions as
to what this library could and should be would be greatly appreciated

:) 