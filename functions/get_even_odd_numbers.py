# functions/get_even_odd_numbers.py
"""
1. Return even numbers from a list of numbers
2. Return odd numbers from a list of numbers
"""
def get_even_numbers(numbers):
    """
    Inline loop through numbers, if divisible by 2, it's even, return modified list
    """
    even_numbers = (x for x in numbers if x % 2 == 0)
    return even_numbers


def get_odd_numbers(numbers):
    """
    Inline loop through numbers, if divisible by 2 filter it out, return modified list
    """
    odd_numbers = filter(lambda num: num % 2, numbers)
    return odd_numbers