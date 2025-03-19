# tests/test_defining_functions.py
"""
Test for defining functions with a variable number of arguments
"""
from functions.defining_functions import (
    function_with_required_positional_arguments,
    function_with_required_positional_argument_and_default_value,
    function_with_default_values, function_with_formal_parameters,
    function_with_slash_and_asterisk_between_parameters
)

def test_function_with_required_positional_arguments():
    """
    Test that the function returns the expected result: {"argument1": 1, "argument2": 2}
    """
    result = function_with_required_positional_arguments(1, 2)
    assert result == {"argument1": 1, "argument2": 2}

def test_function_with_required_positional_argument_and_default_value():
    """
    Test that the function returns the expected result: {"argument1": 1, "argument2": "bar"}
    """
    result = function_with_required_positional_argument_and_default_value(1)
    assert result == {"argument1": 1, "argument2": "bar"}

def test_function_with_default_values():
    """
    Test that the function returns the expected result: {"argument1": 1, "argument2": "bar"}
    """
    result = function_with_default_values()
    assert result == {"argument1": "foo", "argument2": "bar"}

def test_function_with_formal_parameters():
    """
    Test that the function returns the expected result: {"argument1": "foo", "arguments": ["foozbaaz", "goopgaap"], "keywords": [{"foo": "bar"}, {"bar": "baz"}]}
    """
    result = function_with_formal_parameters("foo", "foozbaaz", "goopgaap", foo="bar", bar="baz")
    assert result == {"argument1": "foo", "arguments": ["foozbaaz", "goopgaap"], "keywords": [{"foo": "bar"}, {"bar": "baz"}]}

def test_function_with_slash_and_asterisk_between_parameters():
    """
    Test that the function returns the expected result: {"argument1": 1, "argument2": "bar"}
    """
    result = function_with_slash_and_asterisk_between_parameters(1, 2, keyword_only=3)
    assert result == {"argument1": 1, "argument2": 2, "keyword_only": 3}
    