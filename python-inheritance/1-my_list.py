#!/usr/bin/python3

"""
    Write a class MyList
    wich inherits from list
"""


class MyList(list):
    """
        the class of list
    """

    def print_sorted(self):
        """Print the elements of the list
           in the order
        """
        print(sorted(self))
