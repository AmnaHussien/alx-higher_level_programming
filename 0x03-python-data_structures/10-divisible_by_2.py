#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_li = my_list.copy()
    for j in range(0, len(my_list)):
        if my_list[j] % 2 == 0:
            new_li[j] = 1
        else:
            new_li[j] = 0
    return new_li
