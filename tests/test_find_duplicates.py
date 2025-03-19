# tests/test_find_duplicates.py
"""
Test find duplicates
"""
from functions.find_duplicates import find_duplicates

def test_find_duplicates():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the find_duplicates method.
    """
    test_value_dictionary_for_find_duplicates = {
        0: {
            "input": [3, 7, 2, 9, 4, 7, 6, 5, 4, 7],
            "output": [4, 7] 
        },
        1: {
            "input": ["12", 12, "12", "string"],
            "output": ["12"] 
        },
        2: {
            "input": [-12, 1.234, 1.234, 8, -100000],
            "output": [1.234] 
        }
    }
    for values in test_value_dictionary_for_find_duplicates.values():
        result = find_duplicates(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]