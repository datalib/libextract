def node_json(node):
    return {
        'xpath': node.getroottree().getpath(node),
        'class': node.get('class'),
        'id': node.get('id'),
        'text': node.text_content(),
        'tag': node.tag,
    }


def tabular_json(node_counter_pairs):
    rv = []
    for node, counter in node_counter_pairs:
        json = node_json(node)
        json['contains'] = {e.tag: count for e, count in counter}
        rv.append(json)
    return rv
