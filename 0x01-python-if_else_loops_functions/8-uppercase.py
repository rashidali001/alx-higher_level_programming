#!/usr/bin/python3
def uppercase(str):
    upper_case = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            upper_case = upper_case + chr(ord(i) - 32)
        else:
            upper_case = upper_case + i
    print('{}'.format(upper_case))
