#!/usr/bin/python3
for digit in range(0, 10):
        for ch in range(0, 10):
             if digit == ch or digit > ch:
                 continue
             print(f"{digit}{ch}" + ", " , end = "")
             ch = ch + 1
             if digit > ch:
                 print(f"{digit}{ch}" )
                 break
        digit = digit + 1
