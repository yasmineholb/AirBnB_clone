#!/usr/bin/python3
"""
This module contains BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The class BaseModel defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """ printable reprsentation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        a = {}
        for k, v in self.__dict__.items():
            if k != 'created_at' and k != 'updated_at':
                a[k] = v
        a['__class__'] = self.__class__.__name__
        a['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        a['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return a
