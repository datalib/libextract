Libextract: simple data extraction
==================================

.. image:: https://travis-ci.org/datalib/libextract.svg?branch=master
    :target: https://travis-ci.org/datalib/libextract

::

        ___ __              __                  __
       / (_) /_  ___  _  __/ /__________ ______/ /_
      / / / __ \/ _ \| |/_/ __/ ___/ __ `/ ___/ __/
     / / / /_/ /  __/>  </ /_/ /  / /_/ / /__/ /_
    /_/_/_.___/\___/_/|_|\__/_/   \__,_/\___/\__/


Libextract is a `statistics-enabled <https://github.com/datalib/StatsCounter>`_
extraction library that works on HTML and XML documents, written in Python
and originating from `eatiht <http://rodricios.github.io/eatiht/>`_.


Overview
--------

`libextract.api.extract(document, encoding='utf-8', strategy=ARTICLE_NODE)`
    Given an html *document*, and optionally the *encoding*
    and the *strategy* to use, which defaults to the statistical
    article extraction strategy, return a list of a maximum of
    5 predictions, which is a list of node-metric pairs.


Installation
------------

::

    pip install libextract

Usage
-----

Extracting text-nodes from a wikipedia page:

.. code-block:: python

    from requests import get
    from libextract.api import extract

    r = get('http://en.wikipedia.org/wiki/Information_extraction')
    textnodes = list(extract(r.content))

The predictions returned by the extract function, assuming that you
are using the default strategies are
`HtmlElement <http://lxml.de/lxmlhtml.html>`_ objects (along
with the associated *metric* used to rank each prediction).

Therefore, you can access lxml's methods for post-processing.

.. code-block:: python

    >> print(textnodes[0].text_content())
    Information extraction (IE) is the task of automatically extracting structured information...


Tabular-data extraction is just as easy.

.. code-block:: python

    from libextract.api import ARTICLE_TABLES

    height_data = get("http://en.wikipedia.org/wiki/Human_height")
    tabs = extract(
        height_data.content,
        strategy=ARTICLE_TABLES,
    )

Dependencies
~~~~~~~~~~~~

::

    lxml
    statscounter

Disclaimer
~~~~~~~~~~

This project is still in its infancy; and advice and suggestions as
to what this library could and should be would be greatly appreciated

<<<<<<< HEAD
:) 
=======
:)
>>>>>>> oo-approach
