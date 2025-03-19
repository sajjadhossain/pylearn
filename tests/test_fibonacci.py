# tests/test_fibonacci.py
"""
Test fibonacci function
"""
from functions.fibonacci import fibonaccci

def test_fibonacci():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the fibonacci method.
    """
    test_value_dictionary_for_fibonacci = {
        0: {
            "input": 10,
            "output": [0, 1, 1, 2, 3, 5, 8]
        },
        1: {
            "input": 15,
            "output": [0, 1, 1, 2, 3, 5, 8, 13] 
        },
        2: {
            "input": 2,
            "output": [0, 1, 1] 
        }
    }
    for values in test_value_dictionary_for_fibonacci.values():
        result = fibonaccci(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]