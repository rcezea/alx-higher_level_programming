#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for a in range(x):
            print(my_list[a], end='')
            i += 1
        print()
        return i
    except IOError:
        print()
        return i
