#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv

    if (len(argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        print(1)
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))

    elif operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))

    elif operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))

    elif operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))

    else:
        print('Unkown operator. Available operators: +, -, * and /')
        print(1)
        exit(1)

    print(0)
