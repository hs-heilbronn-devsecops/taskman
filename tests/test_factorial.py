def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(8) == 40320 
    assert factorial(12) == 479001600

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        