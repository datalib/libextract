from pytest import fixture
from lxml import etree
from tests import asset_path


FOO = asset_path('full_of_foos.html')


@fixture
def element():
    return etree.fromstring('<tag><nest>Hi</nest><nest>Bye</nest></tag>')


@fixture
def foo_file(request):
    fp = open(FOO, 'rb')
    request.addfinalizer(fp.close)
    return fp
