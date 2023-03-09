# 0-positive_or_negative.py
check whether a randomly generated number is
positive or negative
## random module
is an in-built module of python which is used to generate random numbers
randint is used with a start of -10 and end of 10 to generate random numbers between -10 and 10
## solution
use if elif statements to check

# 1-last_digit.py
check the last digit of a number
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
## solution
abs() this function in Pyhton returns the absolute value of a number, the absolute value of a number is the magnitude of a number without considering its sing.It returns the positive distance from zero regardless of whether the number is positive or negative
You can use if elif else statement
``` python
#!/usr/bin/python3
import random
number =  random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
print(f"Last digit of {number} is {last} and is {'greater than 5' if last > 5 else '0' if last == 0 else 'less than 6 and not 0'}")
```
# 2-print_alphabet.py
print ASCII alphabet in python in lowercase
in ASCII table lowercase a is 97 and lowercase z is 122
## solution
The requirment is to use string format() method but you can also use chr()
loop from 97 to 122 and use chr() function in python
chr() is a built-in function in Python that returns a string representing a character whose unicode code point is the interger parameter
```python
for i in range(97, 123):
    print(chr(i), end = " ")
```