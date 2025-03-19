# functions/fibonacci.py
"""
1. Fibonacci function
2. Fibonacci generator
"""
def fibonacci(l: int) -> list[int]:
    """
    Take an integer, 
    and return a set of fibonacci integers up to given integer
    """
    sequence = []
    a, b = 0, 1
    while a < l:
        sequence.append(a)
        a, b = b, a+b
    return sequence

def fibonacci_generator():
    """
    A generator function for fibonacci
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        