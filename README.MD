Libextract: simple data extraction
==================================

![image](https://travis-ci.org/datalib/libextract.svg?branch=master)

        ___ __              __                  __
       / (_) /_  ___  _  __/ /__________ ______/ /_
      / / / __ \/ _ \| |/_/ __/ ___/ __ `/ ___/ __/
     / / / /_/ /  __/>  </ /_/ /  / /_/ / /__/ /_
    /_/_/_.___/\___/_/|_|\__/_/   \__,_/\___/\__/


Libextract is a [statistics-enabled](https://github.com/datalib/StatsCounter)
extraction library that works on HTML and XML documents, written in Python
and originating from [eatiht](http://rodricios.github.io/eatiht/).

The philosophy and aim is to provide simple, declaratively composed, and
pipelined functions for users to describe their extraction algorithms.

## Skip to:

* [Overview](#overview)

    * [Coretools](#coretools)
    * [Generators](#generators)
    * [Formatters](#formatters)

* [Usage](#usage)
* [Extraction Algorithms](#extraction-algorithms)
* [Basics of Probability](#basics-of-probability)
* [Maximizing](#maximizing)


Overview
--------

Libextract primarily exists in three modules: ``libextract.coretools``, ``libextract.generators``, and ``libextract.formatters``.

###Coretools

> **pipeline**(*doc*, (*func1*, *func2*,.. *funcN*))

``pipeline`` is the engine of your extraction algorithms. Its [implementation](#TODO) is  simple. To use, pass it two things: an HTML string (ie. ``"<html><head>..</body></html>"``) and a ``tuple`` (or ``list``) of functions.

The basic pattern that ``pipeline`` follows is this: *the output of the first function is the input of the next*.

> **parse_html**(*html_string, encoding*)

``parse_html`` is this library's ignition switch; it's a simple wrapper to [lxml's parse](#TODO) function, exposing just the *encoding* options (defaults to ``utf-8``).

``parse_html`` accepts an HT/XML string, optionally accepts the encoding, and returns an [lxml ElementTree](#TODO) (*etree* for short).

``pipeline`` and ``parse_html`` are almost always used together, like so: ``pipeline(doc, (parse_html,))``

###Generators


> **@iters**(*tags)

 ``@iters`` is a decorator that allows your custom ``pipeline`` function to do two things:

 1. extract nodes based off their tag

 2. apply *per-node* manipulations to those nodes. Skip to [**Usage**](#usage) for examples.


 > **@selects**(xpath)

 ``@selects`` differs from ``@iters`` only in name and selection mechanism - where ``@iters('div', 'p')`` will yield all ``<div>``, ``<p>`` nodes, ``@selects('//div/p')`` will yield all ``<p>`` nodes that exist immediately under a ``<div>`` node. In other words, *extract all ``<p>`` nodes that have a ``<div>`` node as a parent*.

 > **@maximize**(*num_of_results*, key_fn)

 ``@maximize`` is a decorator that will execute a sorting/maximization calculation on a prior "extraction step", where each "step" produces an iterable. For example,

 ```python
# read these next two lines last
# After extracting a list of text-node parents, produce the top 5
# (node, numerical) pairs, using numerical value of returned tuple to sort by
@maximize(5, lambda x: x[1])
@selects("//text()[normalize-space()]") # get_text will now iterate over all text-nodes
def get_text(node):
    return node.getparent(), len(" ".join(node.text_content().split()))
 ```

###Formatters

> **convert_table**(*table_elem*)

``convert_table`` is a combination of fuzzy-logic and prior knowledge of ``<table>`` structures, wrapped into a useful method.

```python
>>> table = convert_table(table_elem)
{'Average female height': ['N/A',
  '159.6 cm (5 ft 3 in)',
  '160.76 cm (5 ft 3 1?2 in)',
  '158.1 cm (5 ft 2 in)',
  '161.8 cm (5 ft 3 1?2 in)',
  '163.8 cm (5 ft 4 1?2 in)',
  ...}
```

Usage
---

Using some of the definitions described above, here are two extraction algorithms that will produce two types of data: main content (news stories, comments, etc.) and tabular data (``<table>`` and the like).

```python
from libextract.core import parse_html, pipeline
from libextract.generators import selects, maximize, iters
from libextract.metrics import StatsCounter
from libextract.xpaths import TEXT_NODES, PARENT_NODES

from requests import get
url = "http://en.wikipedia.org/wiki/Human_height"
r = get(url) # make request, receive response from site

@maximize(5, lambda x: x[1].max())
@selects(PARENT_NODES) # uses table-extracting xpath
def group_parents_children(node):
    return node, StatsCounter([child.tag for child in node])

@maximize(5, lambda x: x[1])
@selects(TEXT_NODES) # uses text-extracting xpath
def group_nodes_texts(node):
    return node.getparent(), len(" ".join(node.text_content().split()))

texts = pipeline(r.content, (parse_html, group_nodes_texts,))

tables = pipeline(r.content, (parse_html, group_parents_children,))
```

``texts`` contains:

```python
>>> texts
[(<Element div at 0x566fe58>, 1540),
 (<Element div at 0x566fe58>, 1262),
 (<Element div at 0x566fe58>, 1248),
 (<Element div at 0x566fe58>, 1133),
 (<Element div at 0x566fe58>, 1062)]
>>> texts[0][0].text_content()
For other uses, see Tall (disambiguation) and Height (disambiguation).
Human height or stature is the distance from the bottom of the feet to
the top of the head in a human body, standing erect. It is measured
using a stadiometer,[1] usually in centimetres when using the metric
system,[2][3] or feet and inches when using the imperial system.[4][5]
```

``tables`` contains:

```python
>>> tables
[(<Element table at 0x562f548>, StatsCounter({'tr': 210})),
 (<Element ol at 0x5672958>, StatsCounter({'li': 155})),
 (<Element span at 0x567aae8>, StatsCounter({'a': 46})),
 (<Element div at 0x56293b8>,
  StatsCounter({'p': 42, 'div': 11, 'h2': 11, 'table': 5, 'ul': 4, <built-in function Comment>: 3, 'h3': 3, 'noscript': 1})),
 (<Element ul at 0x5692458>, StatsCounter({'li': 28}))]
```

---

The next few sections provide brief explanations to some of the ideas and conventions present in libextract.

Extraction Algorithms
---------------------

While libextract provides two useful extraction algorithms (``libextract.ors.article`` and ``libextract.ors.tabular``), what libextract is *really* trying to provide is a set of useful conventions and abstractions (read ``functions`` and ``decorators``) from which to create your algorithms.

The first decorator, named internally as a ``generator`` (?consider changing this name?) is ``@iters``:

```python
@iters('tr') # accepts 1 to n tag names: 'div', 'p', etc.
def get_rows(node): # in one extraction job's lifetime, every <tr> node passes here once
    return node.text_content()

rows = pipeline(doc, (parse_html, get_table_rows)) # returns a list of <tr> nodes
```

There you have it, your first extraction algorithm!

Similarly,

```python
@selects('//tr') # same as above, only in XPath notation
def get_rows(node):
    return node.text_content()
```

Two ways to implement the same algorithm!

Now some of you may be thinking, *Pshh, these guys are throwing around the word "__algorithm__", they don't know what they're talking about.*

In order to rebut comments such as those, a good amount of time was spent trying to encapsulate the *feeling* of creating an algorithm. The product of that labor of love is ``@maximize``.

Before we demonstrate an example use case of ``@maximize``, a couple of things should be addressed about the name (and the concept it's referring to).

###Basics of Probability

Imagine taking the works of your favorite author and creating a frequency distribution of all the words written in those works. Let's call that distribution: __*X*__.

If I asked you to give me the **number** of times the *most common* word appears, what I'm asking you is to find me the __*max*__ of __*X*__.

Or, __*max(X)*__.

Now to wrap up this section, one final piece of (un)necessary jargon is **_argmax_**.

If you ever read **_argmax(X)_** in an *Intro To Probabilistic Machine Learning* book, it's asking you to find the *argument* which yields the __*max(X)*__.

Fast Fact: in practically every book, *__argmax__*(*freq. dist. of words in book*) yields "the".

##Maximizing

Let's consider the problem of extracting the main article of some online news site:

```html
<html>
    <head></head>
    <body>
        <div>
            <article>
                <p>"Our planet is full of soil", says French Prime Minister</p>
                <p>American politicians recoiled, saying "French soil is `le sad`"</p>
                <p>Greece continues to top the charts with highest number of ancient Greek Gods.</p>
                <p>This story's writer clearly has ADHD.</p>
            </article>
        </div>
        <div>
            <div>
                <p>Buy Gold Now!</p>
                <p>Get The Gold Next Door!</p>
                <p>Increase Your Gold!</p>
                <p>Never Goldagain!</p>
            </div>
        <div>
            <footer>
                <p>feeter</p
            </footer>
        </div>
    </body>
</html>
```
#TODO

Consider pointing to rodricios.github.io/eatiht? or explain the algorithm here as it would likely be a good resource for users wanting to push towards the full potential of libextract?

(??O?)?
