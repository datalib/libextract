from functools import partial


UNLIMITED = float('NaN')


def split_node_attr(node, attr):
    """
    Given a *node*, split the *attr* of the node
    into a list of strings, suitable for id/class
    handling.
    """
    return (node.get(attr) or '').split()


get_node_id = partial(split_node_attr, attr='id')
get_node_class = partial(split_node_attr, attr='class')


def node_json(node, depth=0):
    """
    """
    return {
        'xpath': node.getroottree().getpath(node),
        'class': get_node_class(node),
        'text': node.text,
        'tag': node.tag,
        'id': get_node_id(node),
        'children': (
            [node_json(n, depth-1) for n in node] if depth else None
        ),
    }
