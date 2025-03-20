# tests/test_decorators.py
"""
1. Decorator function, a log wrapper
2. Decorator that accepts an argument
"""
def log_execution(func):
    """
    A function that consumes the function and parses the name, arguments and keyword arguments
    then prints the result after cleaning it up a bit, returns the result and then the wrapper
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_object = {
            "executed": f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}",
            "resulted": f"{func.__name__} returned {result}"
        }
        return log_object
    return wrapper

@log_execution
def log_add(a, b):
    """
    A sum function to test our logging wrapper with
    """
    return a + b

def repeat(number_of_times):
    """
    A decorator that accepts an argument,
    number of times, this wrapper should run
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(number_of_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """
    Apply the decorator with arguments
    """
    return f"Hello, {name}!"

def add_method(cls):
    """
    Define a class decorator
    """
    def hello(self):
        """
        Define a method called greet that returns a string manipulation of a provided argument
        """
        return f"Hello, I am {self.name}!"
    cls.hello = hello
    return cls

@add_method
class Person:
    """
    A class to test our decorator with
    """
    def __init__(self, name):
        self.name = name

    def hello(self):
        """
        Placeholder method for Pylint
        """
