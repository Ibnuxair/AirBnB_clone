#!/usr/bin/env python3

"""
This module defines a class named FileStorage
"""


from json import dumps, loads
import os
from models.my_classes import my_classes


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to inst.
    """

    __file_path = 'file.json'
    __objects = {}

    @staticmethod
    def to_json_string(objs_dic):
        """Convert objects dictionary to a JSON string."""

        if objs_dic is None or len(objs_dic) == 0:
            return "{}"

        my_dict = {}
        for obj_id, obj in objs_dic.items():
            if hasattr(obj, 'to_dict'):
                my_dict[obj_id] = obj.to_dict()
            elif isinstance(obj, dict):
                my_dict[obj_id] = obj

        return dumps(my_dict)

    def all(self):
        """ Returns the dictionary __objects. """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file. """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as a_file:
            serialized_objs = FileStorage.to_json_string(FileStorage.__objects)
            a_file.write(serialized_objs)

    def reload(self):
        """ Deserializes the JSON file to __objects. """

        if os.path.exists(FileStorage.__file_path):
            with open(
                    FileStorage.__file_path, "r", encoding="utf-8") as a_file:
                deserialized_objs = loads(a_file.read())

                for k, v in deserialized_objs.items():
                    class_name, obj_id = k.split(".")
                    if class_name in my_classes:
                        obj_class = my_classes[class_name]
                        obj = obj_class(**v)
                        self.new(obj)
