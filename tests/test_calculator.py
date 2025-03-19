# tests/test_calculator.py
"""
Test a Calculator class
for dynamic form:
    - Add
    - Subtract
    - Multiply
    - Divide
and static form:
    - Add
    - Subtract
    - Multiply
    - Divide
"""
import pytest
from classes.calculator import Calculator

def test_add():
    """
    Test dynamic add method
    """
    calc = Calculator(10, 5)
    assert calc.add() == 15

def test_subtract():
    """
    Test dynamic subtract method
    """
    calc = Calculator(10, 5)
    assert calc.subtract() == 5

def test_multiply():
    """
    Test dynamic multiply method
    """
    calc = Calculator(10, 5)
    assert calc.multiply() == 50

def test_divide():
    """
    Test dynamic divide method
    """
    calc = Calculator(10, 5)
    assert calc.divide() == 2.0

def test_divide_by_zero():
    """
    Test dynamic divide method, for divide by zero edge case
    """
    calc = Calculator(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide()

def test_static_add():
    """
    Test static add method
    """
    assert Calculator.static_add(10, 5) == 15

def test_static_subtract():
    """
    Test static subtract method
    """
    assert Calculator.static_subtract(10, 5) == 5

def test_static_multiply():
    """
    Test static multiply method
    """
    assert Calculator.static_multiply(10, 5) == 50

def test_static_divide():
    """
    Test static divide method
    """
    assert Calculator.static_divide(10, 5) == 2.0

def test_static_divide_by_zero():
    """
    Test static divide method, for divide by zero edge case
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.static_divide(10, 0)
