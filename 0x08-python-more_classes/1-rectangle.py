#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    The rectangle class
    """

    def __init__(self, width=0, height=0):
        """ Initiate rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        the self width returned
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width setter
        Throw TypeError and ValueError if some conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("width should be integer")

        if value < 0:
            raise ValueError("width should be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        height getter
        the height returned
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Throw TypeError and ValueError if some conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("height should be an integer")

        if value < 0:
            raise ValueError("height shiould be >= 0")

        self.__height = value
