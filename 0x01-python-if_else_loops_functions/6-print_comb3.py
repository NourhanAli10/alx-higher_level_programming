#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if j == 10 - 1 and i == 10 - 2:
            print("{}{}".format(i, j))
        else:
            print("{}{},".format(i, j), end=" ")
