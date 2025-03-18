from functions.is_palindrome import *

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
    for key, values in test_value_dictionary_for_is_palindrome.items():
        result = is_palindrome_simple(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]

def test_is_palindrome_complex():
    for key, values in test_value_dictionary_for_is_palindrome.items():
        result = is_palindrome_complex(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]