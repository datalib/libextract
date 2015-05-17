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
def etree(foo_file):
    return parse_html(foo_file)
