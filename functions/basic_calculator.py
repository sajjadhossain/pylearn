# functions/basic_calculator.py
"""
Basic calculator functions:
    - Add
    - Subtract
    - Multiply
    - Divide
"""
def add(a: int, b: int) -> int:
    """
    Take 2 integers and return their sum 
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Take 2 integers, subtract argument1 from argument2 and 
    return the total
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Take 2 integers, multiply argument1 by argument2 and 
    return the total
    """
    return a * b

def divide(a: int, b: int) -> int:
    """
    Take 2 integers, divide argument1 from argument2 and 
    return the total
    """
    if b == 0:
        # Return an error when attempting to divide by 0
        raise ValueError("Cannot divide by zero")
    return a / b