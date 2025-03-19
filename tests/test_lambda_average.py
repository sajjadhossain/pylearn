# tests/test_lambda_average.py
"""
Test lambda function in Python
"""
import pytest
from functions.lambda_average import mean

def test_mean():
    """
    Test mean function with lambda
    """
    test_numbers = [2, 5, 6, 7, 85, 3]
    assert mean(test_numbers) == 18.0

def test_divide_by_zero():
    """
    Test dynamic divide method, for divide by zero edge case
    """
    test_numbers = []
    with pytest.raises(ValueError, match="The list of numbers cannot be empty"):
        mean(test_numbers)