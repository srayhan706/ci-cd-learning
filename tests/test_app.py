from app import add,subtract,multipication


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(3, 2) == 1

def test_multipication():
    assert multipication(3,2)==6