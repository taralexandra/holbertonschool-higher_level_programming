#!/usr/bin/python3


"""
function that will print a string with a first_name and eventually a last_name
"""


def say_my_name(first_name, last_name=""):

    """
    Will Print: My name is {first_name} {last_name}

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
