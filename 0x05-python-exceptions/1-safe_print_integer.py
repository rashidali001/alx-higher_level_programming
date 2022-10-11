#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True

    except ValueError:
        print("Not an integer")

safe_print_integer(67.55)