from math import e, pi, tau

from compares import my_gt, my_eq


def test_my_gt():
    """Unit-test my_gt()."""
    assert my_gt(pi, e)
    assert not my_gt(pi, tau)


def test_my_eq():
    """Unit-test my_eq()."""
    assert my_eq(2 * pi, tau)
    assert not my_eq(pi, tau)
