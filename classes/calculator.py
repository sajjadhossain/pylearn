# classes/calculator.py
"""
A Calculator class
istantiates a self with 2 arguments
with 4 accessible methods in dynamic form:
    - Add
    - Subtract
    - Multiply
    - Divide
and 4 accessible methods in static form:
    - Add
    - Subtract
    - Multiply
    - Divide
"""
class Calculator:
    """
    Calculator class istantiated with 2 arguments
    defaulting to 0
    """
    def __init__(self, value_1=0, value_2=0):
        self.value_1 = value_1
        self.value_2 = value_2

    def add(self: int) -> int:
        """
        Take 2 integers and return their sum 
        """
        return self.value_1 + self.value_2

    def subtract(self: int) -> int:
        """
        Take 2 integers, subtract argument1 from argument2 and 
        return the total
        """
        return self.value_1 - self.value_2

    def multiply(self: int) -> int:
        """
        Take 2 integers, multiply argument1 by argument2 and 
        return the total
        """
        return self.value_1 * self.value_2  # Fixed: Changed + to *

    def divide(self: int) -> int:
        """
        Take 2 integers, divide argument1 from argument2 and 
        return the total
        """
        if self.value_2 == 0:
            # Return an error when attempting to divide by 0
            raise ValueError("Cannot divide by zero")
        return self.value_1 / self.value_2

    @staticmethod
    def static_add(a: int, b: int) -> int:
        """
        Take 2 integers and return their sum 
        """
        return a + b

    @staticmethod
    def static_subtract(a: int, b: int) -> int:
        """
        Take 2 integers, subtract argument1 from argument2 and 
        return the total
        """
        return a - b

    @staticmethod
    def static_multiply(a: int, b: int) -> int:
        """
        Take 2 integers, multiply argument1 by argument2 and 
        return the total
        """
        return a * b

    @staticmethod
    def static_divide(a: int, b: int) -> int:
        """
        Take 2 integers, divide argument1 from argument2 and 
        return the total
        """
        if b == 0:
            # Return an error when attempting to divide by 0
            raise ValueError("Cannot divide by zero")
        return a / b