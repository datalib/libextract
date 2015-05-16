from .clean import node_json, table_json, table_list


class ResultSet(list):
    @property
    def nodes(self):
        for node, _ in self:
            yield node

    @property
    def best(self):
        if self:
            return self[0]

    def json(self):
        return [node_json(node) for node in self.nodes]


class TabularResultSet(ResultSet):
    def json(self):
        if self.nodes:
            return table_json(self.best[0])

    def list(self):
        if self.nodes:
            return table_list(self.best[0])
