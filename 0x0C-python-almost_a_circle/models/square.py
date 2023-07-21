#!/usr/bin/python3
""" The Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    """ printable string rep of an instance """
    def __str__(self):
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    """ size, getter and setter """
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.size = args[a]
                if a == 2:
                    self.x = args[a]
                if argmts == 3:
                    self.y = args[argmts]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary rep of a Rectangle"""
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
