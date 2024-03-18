#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = sentence[0]
    if length == 0:
        char = None
        my_tuple = (length, char)
    else:
        my_tuple = (length, char)
    return my_tuple
