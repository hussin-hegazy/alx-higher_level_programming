#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = chaek_tuple(tuple_a)
    tuple_2 = chaek_tuple(tuple_b)
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])


def chaek_tuple(tuple=()):
    len_tuple = len(tuple)
    if len_tuple == 0:
        tuple = 0, 0
    elif len_tuple == 1:
        tuple = tuple[0], 0
    else:
        tuple = tuple[0], tuple[1]
    return tuple
