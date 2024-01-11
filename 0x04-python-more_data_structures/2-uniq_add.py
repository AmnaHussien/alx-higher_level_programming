#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    numb = 0

    for j in uniq_lst:
        numb += j

    return (numb)
