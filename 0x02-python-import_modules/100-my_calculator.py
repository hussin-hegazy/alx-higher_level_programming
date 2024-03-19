#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def calculate(arr):
    if len(arr) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        op = (arr[1])
        if op not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        a = int(arr[0])
        b = int(arr[2])
        print(a, op, b, "=", end=" ")
        if op == '+':
            print(add(a, b))
        elif op == '-':
            print(sub(a, b))
        elif op == '*':
            print(mul(a, b))
        else:
            print(div(a, b))
    exit(0)


if (__name__ == '__main__'):
    calculate(argv[1:])
