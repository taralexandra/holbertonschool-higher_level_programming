#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    bigger_numb = my_list[0]
    for numb in my_list:
        if numb > bigger_numb:
            bigger_numb = numb
    return (bigger_numb)
