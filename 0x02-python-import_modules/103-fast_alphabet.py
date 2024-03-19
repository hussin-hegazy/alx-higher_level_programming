#!/usr/bin/python3
def convrter(x):
    return chr(x)


rng = range(65, 91)
print(*map(convrter, rng), sep="")
print()
