#!/usr/bin/python3
"""
This module contains BaseModel class
"""
import uuid
from datetime import datetime
import models


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
                if k == 'created_at':
                    self.created_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.updated_at = datetime.strptime(
                        v,
                        '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    self.__class__.__name__ = v
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """ printable reprsentation of the object """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

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
        a['created_at'] = self.created_at.isoformat()
        a['updated_at'] = self.updated_at.isoformat()
        return a
