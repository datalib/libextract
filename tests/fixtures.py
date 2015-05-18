import pytest
from tests import asset_path
from libextract.core import parse_html


FOOS_FILENAME = asset_path('full_of_foos.html')


@pytest.fixture
def foo_file(request):
    fp = open(FOOS_FILENAME, 'rb')
    request.addfinalizer(fp.close)
    return fp


@pytest.fixture
def etree():
    with open(FOOS_FILENAME, 'rb') as fp:
        return parse_html(fp, encoding='utf8')
