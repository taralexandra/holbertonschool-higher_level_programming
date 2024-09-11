#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_nbrs = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

    total = 0

    for i in range(len(roman_string) - 1):
        current_value = roman_nbrs[roman_string[i]]
        next_value = roman_nbrs[roman_string[i + 1]]

        if current_value < next_value:
            total -= current_value
        else:
            total += current_value

    total += roman_nbrs[roman_string[-1]]

    return total
