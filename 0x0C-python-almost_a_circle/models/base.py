#!/usr/bin/python3
"""This is Base comp"""
import json
import csv


class Base:
    """The Base class init"""
    __nb_objects = 0

    def __init__(self, id=None):
        """we initialize ithe nstance attributes
        Args:
            id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string rep the of list_dictionaries
        Args:
            list_dictionaries (obj): object
        Returns:
            JSON string rep the of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this writes the JSON string rep of list_objs to file
        Args:
            cls (cls): class
            list_objs (file): list of instances which inherits of Base
        """
        fn = "{:s}.json".format(cls.__name__)
        content = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                content.append(cls.to_dictionary(list_objs[i]))

        with open(fn, mode="w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """this returns list of the JSON string rep json_string
        Args:
            json_string (str): string rep a list of dictionaries
        Returns:
            list of json strings
        """
        a_list = []
        if json_string is not None and json_string != "":
            a_list = json.loads(json_string)
        return a_list

    @classmethod
    def create(cls, **dictionary):
        """this returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary
        Returns:
            instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """this returns a list of instances
        Returns:
            the list of instances
        """
        fn = "{:s}.json".format(cls.__name__)

        try:
            with open(fn, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()  # string of list of dictionaries
            a_list = cls.from_json_string(content_string)  # string to list
            list_instances = []
            for i in range(len(a_list)):  # a_list[i]: dictionary of attributes
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """this serializes in CSV
        Args:
            list_objs (list): the list of objects
        """
        fn = "{:s}.csv".format(cls.__name__)
        content = []
        for i in range(len(list_objs)):
            content.append(cls.to_dictionary(list_objs[i]))  # [{...}, {...}]

        with open(fn, 'w') as a_file:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(a_file, fieldnames=fieldnames)
            writer.writeheader()  # add keys
            writer.writerows(content)  # [{...}, {...}]

    @classmethod
    def load_from_file_csv(cls):
        """this deserializes in CSV
        Returns:
            the list of instances
        """
        fn = "{:s}.csv".format(cls.__name__)
        a_list = []
        try:
            with open(fn, 'r') as a_file:
                reader = csv.DictReader(a_file)  # string of list of dict
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    a_list.append(row)  # str to list
            list_instances = []
            for i in range(len(a_list)):  # a_list[i]: a dictionary of attributes
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances
