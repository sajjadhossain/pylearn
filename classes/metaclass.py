# classes/metaclass.py
# Define the metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with metaclass Meta")
        dct['version'] = 1.0
        return super().__new__(cls, name, bases, dct)

# Define a class using the metaclass
class Animal(metaclass=Meta):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Output when the class is defined:
# Creating class Animal with metaclass Meta

# Define another class using the metaclass
class Dog(metaclass=Meta):
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Output when the class is defined:
# Creating class Dog with metaclass Meta


# Define a simple class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Add a new method to the class dynamically
def roll_over(self):
    return f"{self.name} is rolling over!"

Dog.roll_over = roll_over

# Create an instance of the modified class
my_dog = Dog("Buddy")
print(my_dog.bark())      # Output: Buddy says woof!
print(my_dog.roll_over()) # Output: Buddy is rolling over!

# Define a metaclass
class AddGreeting(type):
    def __new__(cls, name, bases, dct):
        # Add a new method to the class
        dct['greet'] = lambda self: f"Hello, I am {self.name}!"
        return super().__new__(cls, name, bases, dct)

# Define a class using the metaclass
class Person(metaclass=AddGreeting):
    def __init__(self, name):
        self.name = name

# Create an instance of the class
person = Person("Alice")
print(person.greet())  # Output: Hello, I am Alice!

class DictMeta(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        new_attrs = {}
        for key, value in attrs.items():
            if isinstance(value, dict):
                new_attrs.update(value)
            else:
                new_attrs[key] = value
        return super().__new__(mcs, name, bases, new_attrs)

class MyClass(metaclass=DictMeta):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

my_instance = MyClass({'name': 'Alice', 'age': 28})
print(my_instance.name, my_instance.age)