#!/usr/bin/python3
"""
This is a simple base module that will be built on by derived classes.

Returns:
    str: when you print an instance it will return a formatted string.
"""


import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        initializes an instance based on if it does or does not have kwargs.
        if no kwargs it sets up as normal with uuid and datetime.
        if there are kwargs then it initializes based off the dictionaries
        values.
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if '__class__' in kwargs:
                del kwargs['__class__']

            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    kwargs[key] = datetime.fromisoformat(value)

            for key, value in kwargs.items():
                setattr(self, key, value)

        storage.new(self)

    def __str__(self):
        """
        returns a formatted string with the class name, the id, and the dict.
        """

        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        updates the instance attribute updated_at with the current datetime.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        copies the instances __dict__, formats the created_at and updated_at
        strings, adds the __class__ to the dict copy and then returns it.

        Returns:
            dict: returns a dictionary containing all keys/values of
            the instance.
        """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    @classmethod
    def from_dict(cls, inst_dict):
        """
        creates a new instance from a dictionary representation.

        Args:
            inst_dict (dict): dictionary representation of an instance.

        Returns:
            cls: a new instance
        """

        for attr in ['id', 'created_at', 'updated_at']:
            if attr in inst_dict:
                del inst_dict[attr]

        for key, value in inst_dict.items():
            if isinstance(value, dict):
                inst_dict[key] = cls.from_dict(value)

        new_instance = cls(**inst_dict)

        return new_instance
