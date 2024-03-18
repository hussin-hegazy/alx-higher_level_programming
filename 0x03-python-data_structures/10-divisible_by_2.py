#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Nmy_list = []
    for n in my_list:
        if n % 2 == 0:
            Nmy_list.append(True)
        else:
            Nmy_list.append(False)
        return Nmy_list
