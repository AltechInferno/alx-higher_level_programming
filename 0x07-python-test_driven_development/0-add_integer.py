#!/usr/bin/python3
def add_integer(a, b=98):
    """a function that adds 2 numbers"""

    if not a or (type(a) != float and type(a) != int):
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
