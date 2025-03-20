# tests/test_get_even_odd_numbers.py
"""
1. Test return even numbers from a list of numbers
2. Test return odd numbers from a list of numbers
"""
from functions.get_even_odd_numbers import get_even_numbers, get_odd_numbers

test_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_get_even_numbers():
    """
    Use the method with a set and ensure that it returns only numbers divisible by 2
    """
    even_numbers_generated = get_even_numbers(test_set)
    assert list(even_numbers_generated) == [2, 4, 6, 8, 10]

def test_get_odd_numbers():
    """
    Use the method with a set and ensure that it returns only numbers not divisible by 2
    """
    odd_numbers_generated = get_odd_numbers(test_set)
    assert list(odd_numbers_generated) == [1, 3, 5, 7, 9]