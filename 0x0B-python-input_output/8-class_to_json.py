#!/usr/bin/python3
"""
Component for class_to_json.
"""


def class_to_json(obj):
    """
        this returns dictionary rep with simple data structure
    """
    return obj.__dict__
