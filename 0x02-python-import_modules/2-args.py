#!/usr/bin/python3

if __name__ = "__main__":
    import sys

    arg = len(sys.argv) - 1

    if arg == 0:
        print('{} arguments.'.format(arg))

    elif arg == 1:
        print('{} argument:'.format(arg))

    elif arg > 1:
        print('{} arguments:'.format(arg))

    i = 1

    while(i <= arg):
        print('{}: {}'.format(i, sys.argv[i]))
