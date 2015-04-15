class NodeProcessor(object):
    def __init__(self):
        self.mapping = {}

    def register(self, *tags):
        def decorator(fn):
            for tag in tags:
                self.mapping[tag] = fn
            return fn
        return decorator

    def process(self, nodes):
        for node in nodes:
            if node.tag in self.mapping:
                yield self.mapping[node.tag](node)
                continue
            yield node
