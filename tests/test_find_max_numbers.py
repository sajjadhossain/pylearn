# tests/test_find_max_numbers.py
"""
Test find max number from list of numbers
"""
from functions.find_max_number import find_max_number

def test_find_max_number():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the find_max_number method.
    """
    test_value_dictionary_for_find_max_numbers = {
        0: {
            "numbers": [3, 7, 2, 9, 4],
            "max": 9 
        },
        1: {
            "numbers": [12, 1234, 13, 8, 100000],
            "max": 100000 
        },
        2: {
            "numbers": [-12, 1234, 13, 8, -100000],
            "max": 1234 
        }
    }
    for values in test_value_dictionary_for_find_max_numbers.values():
        result = find_max_number(values["numbers"])
        print(f"Expected: {values['max']}, Got: {result}, Value: {values['numbers']}")
        assert result == values["max"]