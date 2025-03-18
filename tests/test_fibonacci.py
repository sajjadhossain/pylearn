from functions.fibonacci import *

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

def test_fibonacci():
    for key, values in test_value_dictionary_for_fibonacci.items():
        result = fibonaccci(values["input"])
        print(f"Expected: {values['output']}, Got: {result}, Value: {values['input']}")
        assert result == values["output"]