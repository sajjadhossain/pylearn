# functions/is_palindrome.py
"""
1. Simple is palindrome implementation
1. Complex is palindrome implementation
"""
from typing import Union

def is_palindrome_simple(s: Union[str, int]) -> bool:
    """
    A simple implementation that
    stringifies the agrument,
    lower cases all characters, and removes whitespaces,
    returns a boolean if it equals its reverse
    """
    s = str(s)
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_palindrome_complex(s: Union[str, int]) -> bool:
    """
    A complex implementation that
    stringifies the agrument,
    lower cases all characters, and removes whitespaces,
    has a loop that goes through the string left to right and
    compares it character by character going right
    returns a boolean if it doesn't equal the reverse and exits the loop
    otherwise returns true
    """
    s = str(s)
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True