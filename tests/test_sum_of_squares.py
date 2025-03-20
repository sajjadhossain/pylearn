# tests/test_sum_of_squares.py
"""
Test a function that takes a list of integers
and returns the sum of their squares
"""
from coderpad.sum_of_squares import sum_of_squares

def test_sum_of_squares():
    """
    Test that the value returned equals the sum of squares
    """
    test_numbers = [2, 3, 4]
    assert sum_of_squares(test_numbers) == 29
