# coderpad/improve_performance.py
"""
Coderpad exercise that asks to improve the quality of the code so it runs in milliseconds \
"""
import random

def generate_random_list(n):
    """
    Generate a list of random n numbers
    """
    # Original Code
    # result = []
    # for i in range(n):
    #     x = random.randint(1,n)
    #     if x not in result:
    #         result.append(x)
    # return result
    #
    # Second Iteration Code
    # result_set = set()
    # while len(result_set) < n:
    #     x = random.randint(1,n)
    #     result_set.add(x)
    # return list(result_set)
    #
    # Solution Code
    return random.sample(range(1, n + 1), n)
