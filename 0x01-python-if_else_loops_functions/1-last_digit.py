#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numstr = repr(number)
    last_digit = -abs(int(numstr[-1]))
    if last_digit > 5:
        print(f"the last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"the last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit != 0:
        print(f"the last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    numstr = repr(number)
    last_digit = int(numstr[-1])
    if last_digit > 5:
        print(f"the last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"the last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit != 0:
        print(f"the last digit of {number} is {last_digit} and is less than 6 and not 0")
