from libextract.html.article import get_node_length_pairs, node_text_length


def test_node_text_length(etree):
    res = etree.xpath('//body/article/div')
    for node in res:
        assert node_text_length(node) == 4
    assert res


def test_get_node_length_pairs(etree):
    u = list(get_node_length_pairs(etree))
    assert len(u) == 10

    for node, score in u:
        assert node.tag in {'article', 'body'}
        assert score in {4, 14}
