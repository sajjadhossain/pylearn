# classes/calculator.py
class Calculator:
    def __init__(self, value_1=0, value_2=0):
        self.value_1 = value_1
        self.value_2 = value_2

    def add(self):
        return self.value_1 + self.value_2

    def subtract(self):
        return self.value_1 - self.value_2

    def multiply(self):
        return self.value_1 * self.value_2  # Fixed: Changed + to *

    def divide(self):
        if self.value_2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.value_1 / self.value_2

    @staticmethod
    def static_add(a, b):
        return a + b

    @staticmethod
    def static_subtract(a, b):
        return a - b

    @staticmethod
    def static_multiply(a, b):
        return a * b

    @staticmethod
    def static_divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b