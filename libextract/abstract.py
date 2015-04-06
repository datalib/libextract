from collections import Counter


def extract_text(finder):
    pairs = finder.get_pairs()
    histogram = Counter()

    for node, score in pairs:
        histogram[node] += score

    best_node, _ = histogram.most_common(1)[0]
    return finder.get_final_text(best_node)


class Finder(object):
    def __init__(self, document):
        self.document = document

    def get_pairs(self):
        return []

    def get_final_text(self, node):
        return ''
