#!/usr/bin/python3
""" This module defines a class named FileStorage"""
import importlib
import json
import os
from models.base_model import BaseModel
import models


class FileStorage():
    """ This class serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ This method sets keys and values for a dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def update(self, obj, key, value):
        """ This method removes an instance and saves to json file"""
        if not hasattr(obj, '__dict__'):
            raise ValueError("obj must be an object instance, got '{}".format(
                type(obj).__name__))
        setattr(obj, key, value)
        models.storage.save(self)

    def remove(self, key):
        """ This method removes instance and saves to json file"""
        del FileStorage.__objects[key]
        models.storage.save(self)

    def save(self):
        """ This method serializes __objects to the json file"""
        serial_objects = {}
        for key, obj in self.__objects.items():
            if hasattr(obj, 'to_dict'):
                serial_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serial_objects, f)

    def reload(self):
        """ This method deserializes the json file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    obj = eval(obj_dict['__class__'])(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
