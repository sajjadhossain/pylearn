# tests/test_count_frequency.py
"""
1. Test count word frequency in a string.
2. Test count value frequency in object, list or string
"""
from functions.count_frequency import word_frequency, value_frequency

def test_word_frequency():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the word_frequency method.
    """
    test_value_dictionary_for_count_word_frequency = {
        0: {
            "input": "hellow hello hey hello hi hey",
            "output": {
                "hellow": 1,
                "hello": 2,
                "hey": 2,
                "hi": 1,
            }
        },
        1: {
            "input": "11 11.11 21.11 21 11",
            "output": {
                "11": 2,
                "11.11": 1,
                "21.11": 1,
                "21": 1,
            }
        }
    }
    for values in test_value_dictionary_for_count_word_frequency.values():
        result = word_frequency(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]

def test_value_frequency():
    """
    Using the array of test values,
    assert each mutation for the expected result,
    for the value_frequency method.
    """
    test_value_dictionary_for_count_value_frequency = {
        0: {
            "input": [1, 2, 3],
            "search": 4,
            "output": 0
        },
        1: {
            "input": ["apple", "banana", "apple", "orange"],
            "search": "apple",
            "output": 2
        },
        2: {
            "input": "hello world",
            "search": "l",
            "output": 3
        },
        3: {
            "input": [1, 2, 3, 4, 2, 2, 3, 1],
            "search": 2,
            "output": 3
        }
    }
    for values in test_value_dictionary_for_count_value_frequency.values():
        result = value_frequency(values["input"], values["search"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}, Search: {values['search']}")
        assert result == values["output"]