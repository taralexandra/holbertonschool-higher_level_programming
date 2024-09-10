#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set()
    for numb in my_list:
        unique_set.add(numb)
    return sum(unique_set)
