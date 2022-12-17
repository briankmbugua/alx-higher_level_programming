#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ["+", "-", "*", "/"]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if sys.argv[2] == operators[0]:
            result = add(a, b)
        elif sys.argv[2] == operators[1]:
            result = sub(a, b)
        elif sys.arg[2] == operators[2]:
            result = mul(a, b)
        elif sys.argv[2] == operators[3]:
            result = div(a, b)

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
