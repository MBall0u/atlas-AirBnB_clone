#!/usr/bin/python3
"""
This is a simple base module that will be built on by derived classes.

Returns:
    str: when you print an instance it will return a formatted string.
"""


import uuid
from datetime import datetime

class BaseModel:
    """
    this is a simple class that will have derived classes pull from it.
    """

    def __init__(self):
        """
        initializes an instance by giving it a unique id and setting the time
        it was created at.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
