UNLIMITED = float('NaN')


def node_json(node, depth=0):
    return {
        'xpath': node.getroottree().getpath(node),
        'class': node.get('class', '').split(),
        'text': node.text,
        'tag': node.tag,
        'id': node.get('id', '').split(),
        'children': (
            [node_json(n, depth-1) for n in node] if depth else None
        ),
    }
