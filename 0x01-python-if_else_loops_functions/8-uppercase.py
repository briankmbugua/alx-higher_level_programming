#!/usr/bin/python3
def uppercase(str):
    for i in str:
        val = i
        if ord(i) in range(97, 123):
            val = chr(ord(i) - 32)
        print("{}".format(val), end="")
    print()
