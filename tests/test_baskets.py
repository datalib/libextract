from libextract.baskets import basket_parent_and_lengths


def test_basket_parent_and_lengths(etree):
    u = list(basket_parent_and_lengths(etree))
    assert len(u) == 10

    for node, score in u:
        assert node.tag in {'article', 'body'}
        assert score in {4, 14}
