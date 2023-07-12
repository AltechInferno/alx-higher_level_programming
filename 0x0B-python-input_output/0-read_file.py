#!/usr/bin/python3
"""
0-read_file component
"""

def read_file(filename=""):
    """
    read_file - this reads a text file and prints it to stdout
    Args:
        filename: the name of the file
    """
    with open(filename, "r", encoding="UTF-8") as fn:
        for line in fn:
            print(line, end="")
