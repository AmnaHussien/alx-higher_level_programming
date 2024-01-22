#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        for x in range(my_list):
            print(my_list[x])
except:
    print("\n")
