#!/usr/bin/python3
i = "abcdefghijklmnopqrstuvwxyz"
for index in range(len(i)):
    if i[index] == 'q' or i[index] == 'e':
        continue
    print(i[index], end = "")
    index = index + 1
