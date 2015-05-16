from .clean import node_json, table_json, table_list


class ResultSet(object):
    def __init__(self, result):
        self.result = result

    def __iter__(self):
        for item in self.result:
            yield item

    @property
    def nodes(self):
        for node, _ in self:
            yield node

    def json(self):
        return [node_json(node) for node in self.nodes]
