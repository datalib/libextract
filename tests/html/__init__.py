from libextract.html import parse_html


def test_parse_html(foo_file):
    etree = parse_html(foo_file)
    divs = etree.xpath('//body/article/div')

    assert all(k.text == 'foo.' for k in divs)
    assert len(divs) == 9
