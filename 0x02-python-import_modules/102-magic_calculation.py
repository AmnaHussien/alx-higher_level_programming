#!/usr/bin/python3


def magic_calculation(i, j):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if i < j:
        k = add(i, j)
        for m in range(4, 6):
            k = add(k, m)
        return (k)
    else:
        return(sub(i, j))
