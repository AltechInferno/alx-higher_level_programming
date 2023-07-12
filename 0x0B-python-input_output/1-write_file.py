#!/usr/bin/python3
"""Component containing the write_file function"""


def write_file(filename="", text=""):
    """This writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): the name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as fn:
        """This returns the number of characters written to a file."""
        return fn.write(text)
