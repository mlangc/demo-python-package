from complexlib import this_fun, that_fun


def test_this_fun():
    assert this_fun(1, 2) == 2


def test_that_fun():
    assert that_fun(1, 2) == 3
