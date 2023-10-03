#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            print("{}".format(chr(i)))

