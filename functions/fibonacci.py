# functions/fibonacci.py
"""
Fibonacci function
"""
def fibonaccci(l: int) -> list[int]:
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