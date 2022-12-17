#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    new_dict = {}
    for i in keys:
        new_dict[i] = a_dictionary[i]
    for i in new_dict:
        print("{}: {}".format(i, new_dict[i]))
