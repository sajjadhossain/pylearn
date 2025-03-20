# functions/lambda_sort.py
"""
A lambda function that sorts by value
"""
def sort_data(data, sort_by):
    """
    Use sorted method and lambda to return a sorted object by sort_by value
    """
    sorted_data = sorted(data, key=lambda x: x[sort_by])
    return sorted_data
