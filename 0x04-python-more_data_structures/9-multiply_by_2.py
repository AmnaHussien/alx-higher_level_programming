#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dir = a_dictionary.copy()
    lst_keys = list(nw_dir.keys())

    for j in lst_keys:
        nw_dir[j] *= 2
    return (nw_dir)
