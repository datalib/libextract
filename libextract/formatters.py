def node_json(node, depth=0):
    json = {
        'xpath': node.getroottree().getpath(node),
        'class': node.get('class'),
        'text': node.text,
        'tag': node.tag,
        'id': node.get('id'),
    }
    if depth:
        json['children'] = [node_json(n, depth-1) for n in node]
    return json


def tabular_json(node_counter_pairs):
    rv = []
    for node, counter in node_counter_pairs:
        json = node_json(node)
        json['contains'] = {e.tag: count for e, count in counter}
        rv.append(json)
    return rv
