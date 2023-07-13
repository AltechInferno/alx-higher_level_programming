#!/usr/bin/python3
"""
append_after component
"""


def append_after(filename="", search_string="", new_string=""):
    '''inserting text after the search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as fn:
        lines = fn.readlines()
        j = 0
        while j < len(lines):
            if search_string in lines[j]:
                lines[j:j + 1] = [lines[j], new_string]
                j += 1
            j += 1
    with open(filename, "w", encoding="utf-8") as fn:
        fn.writelines(lines)
