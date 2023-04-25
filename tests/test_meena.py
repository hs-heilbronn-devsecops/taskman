def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0
    assert multiply(-4, 7) == -28
    assert multiply(10, 2) == 20
    assert multiply(2.5, 3) == 7.5
