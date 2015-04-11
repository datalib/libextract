from __future__ import absolute_import
"""
A submodule providing "pruning" functions.

BACKGROUND:

The extraction algorithms require HT/XML tree traversals.

Before we *analyze* the frequency distributions of some particular
element, which we'll refer to as the "prediction phase", we must
first *prune* for nodes (lxml.html.HtmlElement) and *quantify* some
measurement (numerical or collections.Counter).

What this submodule provides is a decorator called *pruner* and some
predefined pruners.

The usecase is the following:

The user want's to *measure* "something"; he or she can either
import our builtin's (libextract.quantifiers), or they can create
their "quantifier" within a custom function, which they would then
decorate with *pruner*.

For example, if we were to not know that the*text_length* quantifier
existed, we would simply create our own, under the following protocols:

```python
    from libextract.pruners import pruner
    from libextract.html._xpaths import NODES_WITH_TEXT

    # INPUTS
    # "node" must declared, selector must be given as keyword argument
    # user must assume it is an lxml.html.HtmlElement object
    @pruner
    def my_pruner(node, selector=NODES_WITH_TEXT):
        text = node.text
        textlen = len(' '.join(text.split())) if text else 0
        return node.getparent(), textlen
    # OUTPUTS
    # lxml.html.HtmlElement, numerical or collections.Counter
```
"""

from functools import wraps

from libextract.html.xpaths import SELECT_ALL, NODES_WITH_TEXT
from libextract.quantifiers import count_children, text_length


def pruner(selector):
    def decorator(func):
        @wraps(func)
        def quantifier(etree):
            for node in etree.xpath(selector):
                yield func(node)
        return quantifier
    return decorator


@pruner(selector=SELECT_ALL)
def subnode_count_pruner(node):
    """
    Given an *etree*, returns an iterable of parent
    to child node frequencies (collections.Counter) pairs.
    """
    return node, count_children(node)


@pruner(selector=NODES_WITH_TEXT)
def subnode_textlen_pruner(node):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    return node.getparent(), text_length(node)


def basket():
    pass
