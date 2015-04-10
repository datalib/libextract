UNLIMITED = float('NaN')


def node_json(node, depth=0):
    return {
        'xpath': node.getroottree().getpath(node),
        'class': (node.get('class') or '').split(),
        'text': node.text,
        'tag': node.tag,
        'id': (node.get('id') or '').split(),
        'children': (
            [node_json(n, depth-1) for n in node] if depth else None
        ),
    }
