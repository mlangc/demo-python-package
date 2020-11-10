import simplelib


def test_simple_fun():
    assert simplelib.simple_fun(2) == 4


def test_get_version():
    assert simplelib.get_version()
