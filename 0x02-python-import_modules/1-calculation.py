#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    i = 10
    j = 5

    print("{} + {} = {}".format(i, j, add(i, j)))
    print("{} - {} = {}".format(i, j, sub(i, j)))
    print("{} * {} = {}".format(i, j, mul(i, j)))
    print("{} / {} = {}".format(i, j, div(i, j)))
