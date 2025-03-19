# functions/defining_functions.py
"""
It is also possible to define functions with a variable number of arguments. 
There are three forms, which can be combined.
The most useful form is to specify a default value for one or more arguments. 
This creates a function that can be called with fewer arguments than it is defined to allow.
"""
def function_with_required_positional_arguments(arg1: any, arg2: any) -> any:
    """
    Take an argument and return it simply
    """
    return {"argument1": arg1, "argument2": arg2}

def function_with_required_positional_argument_and_default_value(arg1: any, arg2="bar") -> any:
    """
    Take an argument and return it simply, only require 1
    """
    return {"argument1": arg1, "argument2": arg2}

def function_with_default_values(arg1="foo", arg2="bar") -> any:
    """
    Take an argument and return it simply, require none
    """
    return {"argument1": arg1, "argument2": arg2}

def function_with_formal_parameters(arg1: any, *arguments, **keywords) -> any:
    """
    Take all arguments and keywords and return them simply, accept any arguments, any keywords.
    """
    args = []
    kws = []

    for arg in arguments:
        args.append(arg)

    for key, value in keywords.items():
        kws.append({key: value})

    return {"argument1": arg1, "arguments": args, "keywords": kws}

def function_with_slash_and_asterisk_between_parameters(arg1: any, /, arg2: any, *, keyword_only: any) -> any:
    """
    Take all arguments and keywords and return them simply
    """
    return {"argument1": arg1, "argument2": arg2, "keyword_only": keyword_only}
