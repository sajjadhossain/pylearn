# tests/test_metaclass.py
"""
1. Test our meta class that was defined independently
2. Test our class using the meta class
3. Test adding a class dynamically and using the meta class
"""
from classes.metaclass import (
    Animal,
    Dog,
    Person,
    PersonDictionary,
    Meta,
    AddGreeting,
    DictMeta
)

def test_animal_metaclass():
    """
    Test that when we define an Animal, the wrapper works
    """
    dog = Animal("Dog")
    assert Animal.version == 1.0
    assert dog.speak() == "Dog makes a sound."
    assert dog.eat() == "Dog is eating."

def test_dog_metaclass():
    """
    Test that when we define a Dog using the meta class, the wrapper works
    """
    charlie = Dog("Charlie")
    assert Dog.version == 1.0
    assert charlie.bark() == "Charlie says woof!"
    assert charlie.chew() == "Charlie says nom nom!"

def test_dog_adding_class():
    """
    Test that when we add a class to Dog it uses the meta class as well
    """
    def roll_over(self):
        """
        Add a new method to the class dynamically
        """
        return f"{self.name} is rolling over!"
    
    charlie = Dog("Charlie")
    Dog.roll_over = roll_over
    assert Dog.version == 1.0
    assert charlie.roll_over() == "Charlie is rolling over!"

def test_creating_instance_of_metaclass():
    """
    Test that when we create an instance of an existing meta class,
    the methods are inherited
    """
    sajjad = Person("Sajjad")
    assert sajjad.greet() == "Hello, I am Sajjad!"
    assert sajjad.wave_hello() == "Sajjad waves hello at you!"
    assert sajjad.wave_goodbye() == "Sajjad waves goodbye at you!"

def test_creating_instance_of_metadictionary():
    """
    Test that I can add dictionary key values as needed to my class
    """
    meta_dictionary = PersonDictionary({"id": "Sajjad", "age": 36})
    assert meta_dictionary.id == "Sajjad"
    assert meta_dictionary.age == 36

def test_meta_minimal_class():
    """
    Test that the Meta metaclass works with a minimal class definition
    """
    class Minimal(metaclass=Meta):
        """
        Class added to test minimal class configuration
        """

    assert Minimal.version == 1.0

def test_add_greeting_no_name():
    """
    Test that the AddGreeting metaclass works even if the class doesn't define a name attribute
    """
    class NoName(metaclass=AddGreeting):
        """
        Class added to test NoName class
        """
        name: callable

        greet: callable

    instance = NoName()
    instance.name = "Test"
    assert instance.greet() == "Hello, I am Test!"

def test_dict_meta_no_dictionary():
    """
    Test that the DictMeta metaclass works even if no dictionary is passed
    """
    class NoDict(metaclass=DictMeta):
        pass

    instance = NoDict()
    assert not hasattr(instance, 'id')
    assert not hasattr(instance, 'age')

def test_person_dictionary_none_data():
    """
    Test that PersonDictionary works when data is None
    """
    instance = PersonDictionary()
    assert instance.id is None
    assert instance.age is None

def test_person_dictionary_kwargs():
    """
    Test that PersonDictionary works with additional keyword arguments
    """
    instance = PersonDictionary(id="Sajjad", age=36)
    assert instance.id == "Sajjad"
    assert instance.age == 36

def test_person_dictionary_invalid_data():
    """
    Test that PersonDictionary handles invalid data gracefully
    """
    instance = PersonDictionary(data="invalid")
    assert not hasattr(instance.id, 'id')
    assert not hasattr(instance.age, 'age')

def test_person_dictionary_placeholder_methods():
    """
    Test the placeholder methods in PersonDictionary
    """
    instance = PersonDictionary()
    assert instance.print_person() is None
    assert instance.share_person() is None

def test_meta_non_default_attributes():
    """
    Test that the Meta metaclass works with non-default attributes
    """
    class Clazz(metaclass=Meta):
        """
        Test Meta Metaclass with Non-Default Attributes
        """
        custom_attr = "test"
        version = 0.0

        def print_person(self):
            """
            Temporary function to supress warning
            """

        def share_person(self):
            """
            Temporary function to supress warning
            """

    assert Clazz.version == 1.0
    assert Clazz.custom_attr == "test"

def test_add_greeting_override():
    """
    Test that the AddGreeting metaclass works even if the class overrides the greet method
    """
    class CustomGreet(metaclass=AddGreeting):
        """
         Test AddGreeting Metaclass with a Class That Overrides greet
        """
        def greet(self):
            """
            Test method added to class
            """
            return f"Custom greeting from {self.name}!"

        name: callable

        def print_person(self):
            """
            Temporary function to supress warning
            """

        def share_person(self):
            """
            Temporary function to supress warning
            """

    instance = CustomGreet()
    instance.name = "Test"
    assert instance.greet() == "Hello, I am Test!"

def test_dict_meta_non_dict_attributes():
    """
    Test that the DictMeta metaclass works with non-dictionary attributes
    """
    class NonDict(metaclass=DictMeta):
        """
        Test DictMeta Metaclass with Non-Dictionary Attributes
        """
        non_dict_attr = "test"

    assert NonDict.non_dict_attr == "test"

def test_person_dictionary_invalid_kwargs():
    """
    Test that PersonDictionary handles invalid keyword arguments gracefully
    """
    instance = PersonDictionary(invalid_key="invalid_value")
    assert not hasattr(instance.id, 'invalid_key')

def test_person_dictionary_empty_dict():
    """
    Test that PersonDictionary works with an empty dictionary
    """
    instance = PersonDictionary({})
    assert instance.id is None
    assert instance.age is None

def test_person_dictionary_additional_methods():
    """
    Test that PersonDictionary works with additional methods
    """
    instance = PersonDictionary()
    assert instance.print_person() is None
    assert instance.share_person() is None
