"""Geometric mean & Harmonic mean"""


def geometric_mean(collection):
    """Calculate geometric mean from values in collection.

    Definition:
    https://en.wikipedia.org/wiki/Geometric_mean
    """
    q= 1 
    n = len(collection)
    for i in (collection):
        q=q * i 
    return q ** (1/n)





def harmonic_mean(collection):
    """Calculate harmonic mean from values in collection.

    Definition:
    https://en.wikipedia.org/wiki/Harmonic_mean
    """
    s = 0
    n = len(collection)
    for i in (collection):
        s += (1/i)
    return n / s



# Remember to run tests with:
# pytest ex2.py

# Fixtures - pytest provides data for our tests automatically

from pytest import fixture, approx


@fixture
def collection1():
    return [2, 2]

@fixture
def collection2():
    return [1, 2, 3, 4, 5]

@fixture
def collection3():
    return [2, 2, 5, 7]


def test_geometric(collection1, collection2, collection3):
    assert geometric_mean(collection1) == 2.0

    # how to test floats with rounded-up values:
    assert abs(geometric_mean(collection2) - 2.6052) < 0.001
    # otherwise we'd have to compare with (full) correct value:
    # assert geometric_mean(collection2) == 2.605171084697352

    # another good way of testing approximate values is to use `pytest.approx`:
    assert geometric_mean(collection3) == approx(3.4398, 0.001)


def test_harmonic(collection1, collection2, collection3):
    assert harmonic_mean(collection1) == 2.0
    assert harmonic_mean(collection2) == approx(2.1897,0.001)
    assert harmonic_mean(collection3) == approx(2.9787,0.001)
