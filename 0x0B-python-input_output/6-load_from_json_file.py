#!/usr/bin/python3
"""
6-load_from_json_file component
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - this loads an obj from a JSON file.
    Args:
        filename: name of the file
    """
    with open(filename, "r") as fn:
        my_obj = json.load(fn)
        return my_obj
