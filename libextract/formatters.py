def node_json(node, depth=0):
    json = {
        'xpath': node.getroottree().getpath(node),
        'class': node.get('class', '').split(),
        'text': node.text,
        'tag': node.tag,
        'id': node.get('id', '').split(),
    }
    if depth:
        json['children'] = [node_json(n, depth-1) for n in node]
    return json


def tabular_json(node_counter_pairs, **opts):
    rv = []
    for node, counter in node_counter_pairs:
        json = node_json(node)
        hits = json['contains'] = {}
        for elem, count in counter:
            hits[elem.tag] = child = node_json(elem, **opts)
            child['count'] = count
        rv.append(json)
    return rv
