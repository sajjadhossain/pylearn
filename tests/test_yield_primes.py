# tests/test_yield_primes.py
"""
Test function to yield primes
"""
from functions.yield_primes import primes

def test_yield_primes():
    """
    Test that the generator returns an object that contains all prime numbers within a certain limit
    """
    test_limit = 20
    prime_numbers = list(primes(test_limit))
    assert prime_numbers == [2, 3, 5, 7, 11, 13, 17, 19]
    