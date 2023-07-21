#!/usr/bin/python3

"""Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits class Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ construnctor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ width getter and setter """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """height getter and setter """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("heigth must be an integer")
        if height <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = height

    """ x getter and setter """
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """ y getter and setter """
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """ Public comp """

    def area(self):
        """ area value of the Rectangle instance """
        return (self.__height * self.__width)

    def display(self):
        """ Prints in stdout the Rectangle instance with character # """
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            print(self.__x * " " + '#' * self.__width)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.__width = args[arguments]
                if arguments == 2:
                    self.__height = args[arguments]
                if arguments == 3:
                    self.__x = args[arguments]
                if arguments == 4:
                    self.__y = args[arguments]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """ printable string rep of an instance """
    def __str__(self):
        """ It returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """ dictionary rep of a Rectangle"""
        return ({'id': self.id, 'x': self.x, 'height': self.height,
                'width': self.width, 'y': self.y})