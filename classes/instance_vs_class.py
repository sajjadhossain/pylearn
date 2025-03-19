# classes/instance_vs_class.py
"""
A class method is a method that is bound to the class and not the instance of the class. 
It can be called on the class itself, without the need to create an instance of the class. 
An instance method, on the other hand, is bound to the instance of the class 
and can only be called on an instance of the class.
"""
class InstanceVsMethod:
    """
    Class methods are bound to the class and can be called on the class itself or an instance. 
    They are typically used for class-level operations.
    """
    # Class attribute
    class_attribute = "Goodbye"

    def __init__(self, value):
        # Instance attribute
        self.instance_attribute = value

    # Instance method
    def instance_method(self):
        """
        Instance method
        """
        return f"I am an instance method. My instance attribute is {self.instance_attribute}"

    # Class method
    @classmethod
    def class_method(cls):
        """
        Class method
        """
        return f"I am a class method. My class attribute is {cls.class_attribute}"
