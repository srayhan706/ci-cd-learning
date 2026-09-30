from app import add, subtract, multipication


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multipication():
    assert multipication(4, 5) == 20