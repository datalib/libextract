from pytest import fixture
from lxml import etree


@fixture
def element():
    return etree.fromstring('<tag><nest>Hi</nest><nest>Bye</nest></tag>')
