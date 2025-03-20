# coderpad/array_string.py
"""
From CoderPad exercise, a function that takes a string
and returns all characters in a list
"""
def string_to_array(string: str) -> list[str]:
    """
    Take string and return list
    """
    string_to_list = []
    for character in string:
        string_to_list.append(character)

    return string_to_list
