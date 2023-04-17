#!/usr/bin/python3
"""
This class represents the base of all other classes in this project
"""


import json
import csv


class Base:
    """This defines a class named Base"""

    __nb_objects = 0
    """This is a private class attribute"""

    def __init__(self, id=None):
        """initialising thepublic attribute id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns serialised list_dictionaries into a JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Deserialises JSON string of list_objs to a file"""

        filename = cls.__ name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([obj.to_dictionary))
                    for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation"""
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """The module returns an instance with all attribute already set"""
        if cls.__name__ == "Square":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This class method returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                string = f.read()
        except FileNotFoundError:
            return []

        object_list = cls.from_json_string(string)
        return [cls.create(**obj) for obj in object_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize in CSV definition"""
        filename = cls.__name__ +".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as f:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv.writer(f).writerow\
               ([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    csv.writer(f).writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserialize from csv"""
        instances = []
        filename = cls.__name__ + ".csv"


        with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = {"id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row[2]),
                                "x": int(row[3]),
                                "y": int(row[4])}
                elif cls.__name__ == "Square":
                    instance = {"id": int(row[0]),
                                "size": int(row[1]),
                                "x": int(row[2]),
                                "y": int(row[3])}
                diction = cls.create(**instance)
                instances.append(diction)
        return instances
