# coderpad/sum_of_squares.py
"""
From CoderPad exercise, a function that takes a list of integers
and returns the sum of their squares
"""
def sum_of_squares(numbers: list[int]):
    """
    Take numbers, loop through them
    add the sqaure values to a list, and return the list
    """
    numbers_squared = []
    for integer in numbers:
        numbers_squared.append(integer**2)

    return sum(numbers_squared)
