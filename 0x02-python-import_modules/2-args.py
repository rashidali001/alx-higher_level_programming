#!/usr/bin/python3
import sys

arg = len(sys.argv) - 1

if arg == 0:
    print('{} arguments.'.format(arg))

if arg == 1:
    print('{} argument:'.format(arg))

if arg > 1:
    print('{} arguments:'.format(arg))

i = 1

while(i <= arg):
    print('{}: {}'.format(i, sys.argv[i]))
    i += 1
