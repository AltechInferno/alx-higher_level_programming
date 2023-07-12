#!/usr/bin/python3
"""A func that Locks a class against props"""


class LockedClass:
    """a locked class that
    prevents the creaion of another prop
    """

    __slots__ = ["first_name"]
