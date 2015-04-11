from libextract.quantifiers import text_length, count_children


def test_text_length(etree):
    res = etree.xpath('//body/article/div')
    for node in res:
        assert text_length(node) == 4
    assert res

def test_count_children(etree):
    article = etree.xpath('//body/article')[0]
    counter = count_children(article)

    assert len(counter) == 1
    assert counter['div'] == 9
