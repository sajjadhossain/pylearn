import pytest
from classes.calculator import Calculator

def test_add():
    calc = Calculator(10, 5)
    assert calc.add() == 15

def test_subtract():
    calc = Calculator(10, 5)
    assert calc.subtract() == 5

def test_multiply():
    calc = Calculator(10, 5)
    assert calc.multiply() == 50

def test_divide():
    calc = Calculator(10, 5)
    assert calc.divide() == 2.0

def test_divide_by_zero():
    calc = Calculator(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide()

def test_static_add():
    assert Calculator.static_add(10, 5) == 15

def test_static_subtract():
    assert Calculator.static_subtract(10, 5) == 5

def test_static_multiply():
    assert Calculator.static_multiply(10, 5) == 50

def test_static_divide():
    assert Calculator.static_divide(10, 5) == 2.0

def test_static_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.static_divide(10, 0)