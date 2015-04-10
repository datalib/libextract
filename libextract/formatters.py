UNLIMITED = float('NaN')


def split_node_attr(node, attr):
    return (node.get(attr) or '').split()


def node_json(node, depth=0):
    return {
        'xpath': node.getroottree().getpath(node),
        'class': split_node_attr(node, 'class'),
        'text': node.text,
        'tag': node.tag,
        'id': split_node_attr(node, 'id'),
        'children': (
            [node_json(n, depth-1) for n in node] if depth else None
        ),
    }
