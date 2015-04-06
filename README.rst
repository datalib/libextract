libextract
==========

**libextract** is a library for extracting text out of HT/XML
documents using a statistical, functionally pure approach. It
originated from the eatihit_ repository. Usage example:

.. code-block:: python

    from requests import get
    from libextract import extract

    r = get('http://en.wikipedia.org/wiki/Classifier_(linguistics)')
    text = extract(r.content)
