#!/usr/bin/python3
""" this module is about class named base"""
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this function to define instance attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class for create method")
        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """Update instance attributes with the values provided."""
        if args:
            attrs = ["id", "width", "height", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
