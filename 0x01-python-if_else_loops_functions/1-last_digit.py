#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    it = (-number) % 10
else:
    it = number % 10

if number > 0:
    if it == 0:
        print(f'Last digit of {number} is {it} and is 0')
    elif number > 0 and it > 5:
        print(f'Last digit of {number} is {it} and is greater than 5')
    else:
        print(f'Last digit of {number} is {it} and is less than 6 and not 0')
elif number < 0:
    if it == 0:
        print(f'Last digit of {number} is {it} and is 0')
    else:
        print(f'Last digit of {number} is -{it} and is less than 6 and not 0')
elif number == 0:
    print(f'Last digit of {number} is {it} and is 0')
