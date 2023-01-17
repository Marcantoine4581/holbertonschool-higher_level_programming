#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) <= 122 and ord(c) >= 97):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
