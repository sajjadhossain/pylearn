# tests/test_decorators.py
"""
1. Test decorator function, a log wrapper
"""
from classes.decorators import log_add, greet, Person

def test_log_add():
    """
    Test that our decorator returns a wrapped function
    """
    result = log_add(3, 5)
    assert result == {
        'executed': 'Executing log_add with arguments (3, 5) and keyword arguments {}', 
        'resulted': 'log_add returned 8'
    }

def test_greet():
    """
    Test that our decorator runs 3 times as set in the decorater 
    """
    assert greet("Sajjad") == "Hello, Sajjad!"

def test_hello_person():
    """
    Test that our decorated class that adds a dynamic method, works
    """
    person = Person("Sajjad")
    assert person.hello() == "Hello, I am Sajjad!"