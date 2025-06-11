from math import e, pi, tau

from compares import my_eq, my_gt, my_lt


def test_my_gt():
    """Unit-test my_gt()."""
    assert my_gt(pi, e)
    assert not my_gt(2 * pi, tau)


def test_my_eq():
    """Unit-test my_eq()."""
    assert my_eq(2 * pi, tau)
    assert not my_eq(pi, tau)


def test_my_lt():
    """Unit-test my_lt()."""
    assert my_lt(e, pi)
    assert not my_lt(2 * pi, tau)
