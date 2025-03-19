# classes/fibonacci.py
"""
A Fibonacci class with a generator
"""
class FibonacciSequence:
    """
    Init self with a max n
    """
    def __init__(self, max_terms):
        self.max_terms = max_terms

    def generate_fibonacci(self):
        """
        Init self with a max n
        Instantiate with the first two values
        And a count to remember how many times we went through the loop
        A while loop until max_terms is met
            While looping
            - update a, b with valie of b, a + b
            - add to counter
        """
        a, b = 0, 1
        count = 0
        while count < self.max_terms:
            yield a
            a, b = b, a + b
            count += 1
            