#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """
    Class File Storage
    """
    __objects = {}
    __file_path = 'objects.json'

    def all(self):
        """
        gets object info and returtns items in object class
        attribute
        """
        return self.__objects

    def new(self, obj):
        """"
        saves a new object in __objects class attribute
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the content of `__objects` class attribute
        """
        json_dict = {}
        for i, j in self.__objects.items():
            json_dict[i] = j.to_dict()
        with open(self.__file_path, mode="w", encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        Deserializes the JSON file in `__file_path` class attribute
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding='utf-8') as f:
                json_dict = json.load(f)
                from console import classes_c
                for key in json_dict.keys():
                    self.__objects[key] = classes_c[json_dict[key]
                                                    ["__class__"]](
                                                        **json_dict[key])
