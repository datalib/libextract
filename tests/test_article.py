#from libextract.article import get_node_length_pairs
#
#
#def test_get_node_length_pairs(etree):
#    u = list(get_node_length_pairs(etree))
#    assert len(u) == 10
#
#    for node, score in u:
#        assert node.tag in {'article', 'body'}
#        assert score in {4, 14}
