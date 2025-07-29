# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_diff():
    assert subtract(2, 1) == 1
    assert subtract(-1, -2) == -3
