#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_n = number % 10
    else:
        last_n = number % -10
    print(last_n)