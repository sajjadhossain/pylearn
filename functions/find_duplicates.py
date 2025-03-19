# functions/find_duplicates.py
"""
Find duplicates
"""
from typing import Union
 
def find_duplicates(items: list[Union[int, str]]) -> list[Union[int, str]]:
    """
    Take a list of items,
    lopp through items,
    and store each item,
    and if the the item is in seen list,
    add it to duplicates
    """
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)