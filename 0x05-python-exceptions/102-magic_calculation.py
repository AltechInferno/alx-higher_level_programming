#!/usr/bin/python3

def magic_calculation(x, y):
    result = 0
    for index in range(1, 3):
        try:
            if index > x:
                raise Exception('Too far')
            else:
                result += x ** y / index
        except:
            result = y + x
            break
    return (result)
