#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst_ord = list(a_dictionary.keys())
    lst_ord.sort()
    for j in lst_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
