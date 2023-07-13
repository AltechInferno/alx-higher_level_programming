#!/usr/bin/python3
"""
5-save_to_json component
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file -  this writes an Obj to a text file,
                        using a JSON rep:
    Args:
        my_obj:
        filename:
    Return:
    """
    with open(filename, "w") as fn:
        json.dump(my_obj, fn)
