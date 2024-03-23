#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for n in a_dictionary:
        n_dictionary.update({n: a_dictionary[n] * 2})
    return n_dictionary
