#!/usr/bin/python3
for digit in range(0, 10):
        for ch in range(0, 10):
            print(f"{digit}{ch}" + ", " , end = "")
            ch = ch + 1
            if digit == 9 and ch == 9:
                print(f"{digit}{ch}" )
                break
            digit = digit + 1
