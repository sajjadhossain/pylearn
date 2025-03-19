# functions/count_frequency.py
"""
1. Count word frequency in a string.
2. Count value frequency in object, list or string
"""
from typing import Union

def word_frequency(text: str) -> object:
    """
    Take a string, lowercase every character,
    split by space, search for word in list,
    push word: count in to frequency object
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def value_frequency(collection: list[Union[int, str]], value: str) -> int:
    """
    Take an object, list or string,
    wrap a sum function, around an inline counter for:
    the number of times a value appears in the collection
    """
    return sum(1 for item in collection if item == value)
