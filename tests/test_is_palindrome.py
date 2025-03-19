# tests/test_is_palindrome.py
"""
1. Test simple is palindrome implementation
1. Test complex is palindrome implementation
"""
from functions.is_palindrome import is_palindrome_simple, is_palindrome_complex

test_value_dictionary_for_is_palindrome = {
    0: {
        "input": "racecar",
        "output": True 
    },
    1: {
        "input": "madaM",
        "output": True
    },
    2: {
        "input": "happy",
        "output": False 
    },
    3: {
        "input": 11911,
        "output": True 
    },
    4: {
        "input": 1192,
        "output": False 
    }
}

def test_is_palindrome_simple():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the is_palindrom_simple method.
    """
    for values in test_value_dictionary_for_is_palindrome.values():
        result = is_palindrome_simple(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]

def test_is_palindrome_complex():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the is_palindrom_complex method.
    """
    for values in test_value_dictionary_for_is_palindrome.values():
        result = is_palindrome_complex(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]