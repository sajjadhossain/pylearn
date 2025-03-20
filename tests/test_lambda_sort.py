# tests/test_lambda_sort.py
"""
Test the lambda function sorts by value
"""
from functions.lambda_sort import sort_data

def test_lambda_sort():
    """
    Use an object and test calling the function 
    with different sort values returns the correct sorted object
    """
    test_data = [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 21}, {'name': 'Charlie', 'age': 35}]
    assert sort_data(test_data, "name") == [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 21}, {'name': 'Charlie', 'age': 35}]
    assert sort_data(test_data, "age") == [{'name': 'Bob', 'age': 21}, {'name': 'Alice', 'age': 28}, {'name': 'Charlie', 'age': 35}]