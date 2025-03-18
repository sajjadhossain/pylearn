from functions.find_max_number import *

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

def test_find_max_number():
    for key, values in test_value_dictionary_for_find_max_numbers.items():
        result = find_max_number(values["numbers"])
        print(f"Expected: {values['max']}, Got: {result}, Value: {values['numbers']}")
        assert result == values["max"]