from app import add, multiply

def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 100) == 0