#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = roman_string
    item = 0
    result = 0
    for item in range(item, len(roman_number)):
        if item < len(roman_number) - 1 and roman_numerals[roman_number[item]] < roman_numerals[roman_number[item + 1]]:
            result -= roman_numerals[roman_number[item]]
        else:
            result += roman_numerals[roman_number[item]]
    return result
