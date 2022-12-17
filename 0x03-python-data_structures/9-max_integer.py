#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_dgt = 0
        for i in my_list:
            if i > max_dgt:
                max_dgt = i
        return max_dgt
