# functions/find_max_numbers.py
"""
Find max number from list of numbers
"""
def find_max_number(numbers: list[int]) -> int:
    """
    Take a list of integers,
    loop through each number,
    store number if greater than 0,
    then compare to number stored while looping,
    return the largest number
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num