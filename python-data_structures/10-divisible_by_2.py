#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list_resulting = []

    for numb in my_list:
        if numb % 2 == 0:
            new_list_resulting.append(True)
        else:
            new_list_resulting.append(False)
    return new_list_resulting
