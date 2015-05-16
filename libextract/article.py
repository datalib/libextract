from statscounter import StatsCounter
from .metrics import text_length
from .procs import select, rank_with, get_largest, most_common, histogram
from .xpaths import TEXT


def parent_length_pairs(results):
    for node, metric in results:
        yield node.getparent(), metric


STRATEGY = (
    select(TEXT),
    rank_with(text_length),
    histogram(parent_length_pairs),
    most_common(5)
)
