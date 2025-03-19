# functions/lambda_functions.py
"""
Lambda function in Python
"""
from functools import reduce

def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")

    # Calculate the sum using reduce and a lambda function
    total = reduce(lambda x, y: x + y, numbers)

    # Calculate the mean by dividing the total by the number of elements
    average = total / len(numbers)

    return average