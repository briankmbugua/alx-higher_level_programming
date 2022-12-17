#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv[1:]) == 1:
        print("{} argument:".format(len(argv[1:])))
    elif len(argv[1:]) == 0:
        print("{} arguments.".format(len(argv[1:])))
    else:
        print("{} arguments:".format(len(argv[1:])))

    for i in argv[1:]:
        print("{}: {}".format((argv[1:].index(i)) + 1, i))
