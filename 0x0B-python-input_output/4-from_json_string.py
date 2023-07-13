#!/usr/bin/python3
"""
4-from_json_string component
"""
import json


def from_json_string(my_str):
    """
    from_json_string - this returns an object
                    represented by a JSON string:
    Args:
        my_str: a json string to represent
    Return: object
    """
    return json.loads(my_str)
