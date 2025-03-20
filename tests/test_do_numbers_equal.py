# tests/test_do_numbers_equal.py
"""
Test a function that takes 2 integers
and returns a boolean
"""
from coderpad.do_numbers_equal import do_numbers_equal

def test_do_numbers_equal():
    """
    Test the function returns whether or not they equal eachother
    """
    assert do_numbers_equal(2, 5) is False
    assert do_numbers_equal(5, 5) is True
