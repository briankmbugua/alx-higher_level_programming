# 0. 0-run
Write a shell script that run a python script
The Python file name will be saved in the enviromental variable $PYFILE
# solutiom
use shengbang ```(#!/bin/bash)```to get the location of the bash interpreter then run a python3 script located at the path specified in the env variable "$PYFILE"

# 1. 1-run_inline
Write a shell script that run a Python code the code will be saved in the enviromental variable $PYCODE
# SOLUTION
First set an enviromental variable 'PYCODE' with the string value 
'print(f'Best School:{88+10}').The string value assinged to 'PYCODE' is valid python code that can be executed later using a python interpreter

```python3 <<< $PYCODE ```works
The``` '<<<' ```operator is called a 'here string' in shell, and it allows you to pass the contents of a variable as input to a command, in this case the contents of $PYCODE env are passed as input to the 
'python3' which runs the code as Python 3 script

you can also use python interpreter -c option 
```python3 -c "$PYCODE"```
Using double quotes around the env "$PYCODE" allows the shell to subsitute the value of '$PYCODE' env variable before passing it as an argument to the 'python' interpreter
The difference between double quotes and single quotes is that double quotes allow for the expansion of env variables while single quotes preserve the literal value of each character within the quotes

# 2. Hello, print
Write a python script that prints excatly "Programming is like a multilingual puzzle, followed by a new line
Use the function print
To have double quotes in a string use single quotes and vice versa

# 3. 3-print_number.py
print the interger stored in the variable number, followed by Battery street, followed by a new line
# solutuin
since you can't cast number into a srring you can use f-string which allows you to embed expressions inside the string litrals
```{number:d}``` d meeans to format the number as a decimal interger
# 4. 4-print_float.py
print a floating point numner
# solution
use ```{number:.2f}``` to format it as a float to two decimal places
# 5. 5-print_string.py
```str = "Holberton School"```
```print(f"{3*str}\n{str[:9]}")```
print str three times and followed by its first 9 characters
you can use f strings
```(f"{3*str}\n{str[:9]}")```
just normal strings
```(3*str + "\n" + str[:9])``` asterick(*) can be used as a string multiplayer ```3*str``` will return the str three times and ```str[:9]``` is string slicing when the first part of [x:y] or x is left the string is sliced from the end thus [:9] will return the last 9 characters of the string str
# 6. 6-concat.py
concat two given strings, string concantation is done using the + operator you can also use += operator to concantenate the strings and assing the result to the original string
 # solution
 the requirment is that the code be excatly five lines long
 but you can do this too if you just want the output
```python
str1 = "Holberton"
str2 = "School"
print(f"{str1} {str2}")
```
# 7. 7-edges.py
this is the source code given for the question
## requirements
your program should be excatly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
``` python
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```
### solution
i will use object slicing in this case string slicing
```>>> 'ABCD'[0:2]```  == get every single one item between indexes 0 and 2(exclusive)
You can also use step
```>>> 'ABCD'[0:4:2]``` == get every single second element between indexes 0 and 4
negative step argument can be used to reverse the sequence
```"abcd"[::-1] -- 'dcba'```
```python
word = "Holberton"
print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[-2:]}")
print(f"Middle word: {word[1:-1]}")
```
# 8. 8-concat_edges.py
complete this source code to print 'object-oriented programming with Python', followed by a new line
```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
print(str)
```
## solution
```python
str = str[39:66] + str[106:112] + str[:6]
```
you  can also use the find method

# 9. 9-easter_egg.py
print the zen of python
just import this.py and execute

# 10 linked list
will revist

# 11 100.write.py
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1

## solution
we are printing out to stderr therefore the exit code should be zero but it's one since we are setting the status code using python sys module
### example
```python
import sys
sys.stderr.write('Error')
sys.exit(1) # setting the exit status code
```
to check the exit status code use '$?' this is a shell variable in unix-like os's that holds the exit status code of the last executed command
```bash
echo $?
```

# 12 101-compile
compile python code to bytecode which is cross platform and faster to load
## solution
```bash
python3 -m compileall -b $PYFILE
```
this bash script compiles the file stored in the $PYFILE env variable, the script use the python compileall module which provies a way to compile all python source files in a directory to bytecode

-m this option is used to run the module as script in this case the compile module is being run
-b this flag specifies that the generated bytecode files should be optimized for performance

# ByteCode -> Python #1
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```bytecode

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
in python the bytecode is stored in .pyc file   in python 3 the bytecode files are stored in a folder named __pycache__.This folder is automatically created when you try to import another file that you created however it will not be created if we don't import another file in the source code.In that case we can still manaully create it

```bash
python -m compileall pythonfile.py
```
you can also use the compile() function to compile a string that contains the Python source code