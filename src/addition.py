# app.py
# This is a test commit
def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 1) == 4
    assert add(1, -1, 1) == 1
