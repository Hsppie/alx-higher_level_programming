#!/usr/bin/python3
for number in range(100):
    if number == 99:
        print("{}".format(number), end="")
    else:
        print("{number:02},".format(number=number), end=" ")

