#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2) == 0:
        val = chr(i)
    else:
        val = chr(i-32)
    print("{}".format(val), end="")
