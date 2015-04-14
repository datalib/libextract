from pytest import fixture
from lxml import etree as _etree
from libextract.coretools import parse_html
from tests import asset_path


FOO = asset_path('full_of_foos.html')


@fixture
def element():
    return _etree.fromstring('<tag><nest>Hi</nest><nest>Bye</nest></tag>')


@fixture
def foo_file(request):
    fp = open(FOO, 'rb')
    request.addfinalizer(fp.close)
    return fp


@fixture
def etree():
    with open(FOO, 'rb') as fp:
        return parse_html(fp)
