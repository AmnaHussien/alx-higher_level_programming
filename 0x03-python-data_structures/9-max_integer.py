#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    larg = my_list[0]
    for i in range(1, len(my_list)):
        if larg < my_list[i]:
            larg = my_list[i]
        else:
            continue
    return larg
