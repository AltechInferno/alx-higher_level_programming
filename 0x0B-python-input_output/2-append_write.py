#!/usr/bin/python3
"""
append_write component
"""


def append_write(filename="", text=""):
    """
    write_file - This appends a string at the end of a text file (UTF8),
                and returns the number of characters added:
    Args:
        filename: the name of the file
        text: the text to be written
    Return: the  number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as fn:
        return (fn.write(text))
