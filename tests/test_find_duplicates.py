from functions.find_duplicates import *

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

def test_find_duplicates():
    for key, values in test_value_dictionary_for_find_duplicates.items():
        result = find_duplicates(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]