#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        for i in range(x):
            print(my_list[i], end = "")
        print("\n")
        print("nb_print:", x)
except:
    print("\n")
