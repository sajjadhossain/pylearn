# classes/metaclass.py
"""
1. Meta class defined independently
"""
class Meta(type):
    """
    Define a general meta class for our Animal class
    """
    version = 0.0

    def __new__(mcs, name, bases, dct):
        print(f"Creating class {name} with metaclass Meta")
        dct['version'] = 1.0  # Add a 'version' attribute to the class
        return super().__new__(mcs, name, bases, dct)

class Animal(metaclass=Meta):
    """
    Define an Animal class to use the meta class
    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        Speak method for our animal class
        """
        return f"{self.name} makes a sound."

    def eat(self):
        """
        Eat method for our animal class
        """
        return f"{self.name} is eating."

class Dog(metaclass=Meta):
    """
    Define another class using the metaclass
    """
    def __init__(self, name):
        self.name = name

    def bark(self):
        """
        Bark method for our dog class
        """
        return f"{self.name} says woof!"

    def chew(self):
        """
        Chew method for our dog class
        """
        return f"{self.name} says nom nom!"

class AddGreeting(type):
    """
    Define a metaclass that adds a class to another class
    """
    def __new__(mcs, name, bases, dct):
        dct['greet'] = lambda self: f"Hello, I am {self.name}!"
        return super().__new__(mcs, name, bases, dct)

class Person(metaclass=AddGreeting):
    """
    Define a class using the metaclass
    """
    def __init__(self, name):
        self.name = name

    def wave_hello(self):
        """
        Generic function to wave hello
        """
        return f"{self.name} waves hello at you!"

    def wave_goodbye(self):
        """
        Generic function to wave goodbye
        """
        return f"{self.name} waves goodbye at you!"

    greet: callable

class DictMeta(type):
    """
    A meta class that creates a dictionary for any class to use and inherit
    """
    def __new__(mcs, name, bases, attrs, **kwargs):
        new_attrs = {}
        for key, value in attrs.items():
            if isinstance(value, dict):
                new_attrs.update(value)
            else:
                new_attrs[key] = value
        return super().__new__(mcs, name, bases, new_attrs)

class PersonDictionary(metaclass=DictMeta):
    """
    A class that uses the meta class for person dictionary
    """
    id = None

    age = None

    def __init__(self, data=None, **kwargs):
        if data is not None and isinstance(data, dict):
            for key, value in data.items():
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def print_person(self):
        """
        Temporary function to supress warning
        """

    def share_person(self):
        """
        Temporary function to supress warning
        """
