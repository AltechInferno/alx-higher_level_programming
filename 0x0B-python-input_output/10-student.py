#!/usr/bin/python3
"""
  Student Component
"""


class Student:
    """
        A students class that defines a student by:
        Attributes:
            first_name (str): the name of student.
            last_name (str): the name of student.
            age (int): the age of student.
      """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieve a dictionary rep of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            ress = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return ress
        else:
            return self.__dict__
