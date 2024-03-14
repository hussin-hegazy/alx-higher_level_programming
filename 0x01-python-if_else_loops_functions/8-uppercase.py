#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        n_letter = ord(i)
        if n_letter >= 97 and n_letter <= 122:
            n_letter -= 32
        print("{}".format(n_letter), end="")
    print("")
