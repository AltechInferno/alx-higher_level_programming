#!/usr/bin/python3
"""
component for 3-to_json_string
"""
import json


def to_json_string(my_obj):
    """
    to_json_string - this returns the JSON representation of an object (string):
    Args:
        my_obj: is the string to represent
    Return: the json representation
    """
    return json.dumps(my_obj)
