#!/usr/bin/python3
"""
0-read_file component
"""

def read_file(filename=""):
    """
    read_file - read text file, prints it to stdout
    Args:
        filename: the name of the file
    """
    with open(filename, "r", encoding="UTF-8") as fn:
        for line in fn:
            print(line, end="")
