#!/usr/bin/python3
"""
   Student class component.
"""


class Student:
    """
        A students class that defines a student by:
        Attributes:
            first_name (str): the name of student.
            last_name (str): the name of student.
            age (int): the age of student.
        Methods:
            __init__ - this initializes the Student instance.
            to_json - this gets dictionary rep of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieve a dictionary rep of Student.
        """
        return self.__dict__
