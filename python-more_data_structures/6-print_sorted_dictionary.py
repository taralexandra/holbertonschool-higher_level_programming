#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dico = sorted(a_dictionary.keys())
    for key in sorted_dico:
        print(f"{key}: {a_dictionary[key]}")
