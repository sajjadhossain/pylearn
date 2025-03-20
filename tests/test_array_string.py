# tests/test_array_string.py
"""
Test a function that takes a string
and returns all characters in a list
"""
from coderpad.array_string import string_to_array
def test_array_to_string():
    """
    Test string to array return 
    """
    assert string_to_array("hello") == ["h", "e", "l", "l", "o"]
    