#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_string = roman_string.upper()
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in roman_string:
        if i not in roman:
            return 0
    integer_value = 0
    i = 0
    while i < len(roman_string):
        if len(roman_string) == 1:
            for j in roman.keys():
                if str(roman_string[i]) == str(j):
                    integer_value += roman[j]
            break

        if (roman_string[i] == "I" and roman_string[i+1:i+2] == "X") or \
                roman_string[i] == str("I") and \
                roman_string[i+1:i+2] == str("V") or \
                roman_string[i] == str("X") and \
                roman_string[i+1:i+2] == str("L") or \
                roman_string[i] == str("X") and \
                roman_string[i+1:i+2] == str("C") or \
                roman_string[i] == str("C") and \
                roman_string[i+1:i+2] == str("D") or \
                roman_string[i] == str("C") and \
                roman_string[i+1:i+2] == str("M"):
            first = 0
            last = 0
            for j in roman.keys():
                if str(roman_string[i]) == str(j):
                    first = roman[j]
                if str(roman_string[i + 1]) == str(j):
                    last = roman[j]
            integer_value = last - first
            i += 2
            continue

        for j in roman.keys():
            if str(roman_string[i]) == str(j):
                integer_value += roman[j]
        i += 1

    return integer_value
