from pytest import fixture
from tests import asset_path
from libextract.html import parse_html


FOOS_FILENAME = asset_path('full_of_foos.html')


@fixture
def foo_file(request):
    fp = open(FOOS_FILENAME, 'rb')
    request.addfinalizer(fp.close)
    return fp


@fixture
def etree(foo_file):
    return parse_html(foo_file)
