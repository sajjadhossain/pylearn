import pytest
from functions.basic_calculator import add, subtract, multiply, divide

test_value_dictionary_for_addition = {
    0: {
        "value_1": 8,
        "value_2": 2,
        "total": 10,
    },
    1: {
        "value_1": 2.2,
        "value_2": 4.8,
        "total": 7,
    },
    2: {
        "value_1": 458,
        "value_2": 242,
        "total": 700,
    }
}

def test_add():
    for key, values in test_value_dictionary_for_addition.items():
        result = add(values["value_1"], values["value_2"])
        print(f"Expected: {values['total']}, Got: {result}")
        assert result == values["total"]

test_value_dictionary_for_subtraction = {
    0: {
        "value_1": 8,
        "value_2": 2,
        "total": 6,
    },
    1: {
        "value_1": 2.2,
        "value_2": 4.8,
        "total": -2.5999999999999996,
    },
    2: {
        "value_1": 458,
        "value_2": 242,
        "total": 216,
    }
}

def test_subtract():
    for key, values in test_value_dictionary_for_subtraction.items():
        result = subtract(values["value_1"], values["value_2"])
        print(f"Expected: {values['total']}, Got: {result}")
        assert result == values["total"]

test_value_dictionary_for_multiplication = {
    0: {
        "value_1": 8,
        "value_2": 2,
        "total": 16,
    },
    1: {
        "value_1": 2.2,
        "value_2": 4.8,
        "total": 10.56,
    },
    2: {
        "value_1": 458,
        "value_2": 242,
        "total": 110836,
    }
}

def test_multiplication():
    for key, values in test_value_dictionary_for_multiplication.items():
        result = multiply(values["value_1"], values["value_2"])
        print(f"Expected: {values['total']}, Got: {result}")
        assert result == values["total"]

test_value_dictionary_for_division = {
    0: {
        "value_1": 8,
        "value_2": 2,
        "total": 4.0,
    },
    1: {
        "value_1": 2.2,
        "value_2": 4.8,
        "total": 0.45833333333333337,
    },
    2: {
        "value_1": 458,
        "value_2": 242,
        "total": 1.8925619834710743,
    }
}

def test_division():
    for key, values in test_value_dictionary_for_division.items():
        result = divide(values["value_1"], values["value_2"])
        print(f"Expected: {values['total']}, Got: {result}")
        assert result == values["total"]

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

