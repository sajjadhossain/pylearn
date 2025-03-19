# tests/test_instance_vs_class.py
"""
Test instance vs class attributes class
"""
from classes.instance_vs_class import InstanceVsMethod

def test_instance_vs_class():
    """
    Test that instance methods returns:
        I am an instance method. My instance attribute is Hello
    Test that both class methods return:
        I am a class method. My class attribute is Goodbye
    """
    obj = InstanceVsMethod("Hello")
    result1 = obj.instance_method()
    result2 = obj.class_method()
    result3 = InstanceVsMethod.class_method()
    expected_result_from_instance = "I am an instance method. My instance attribute is Hello"
    expected_result_from_class = "I am a class method. My class attribute is Goodbye"
    assert result1 == expected_result_from_instance
    assert result2 == expected_result_from_class
    assert result3 == expected_result_from_class