#!/usr/bin/python3
def print_last_digit(number):
    number_str = str(number)
    last_digit = int(number_str[-1])
    print(last_digit, end="")
    return last_digit

