#!/usr/bin/python3
"""
This module contains FileStorage class
"""
import json


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        k = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            a = {}
            for k, v in FileStorage.__objects.items():
                a[k] = v.to_dict()
            j = json.dumps(a)
            f.write(j)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as f:
                from models.base_model import BaseModel
                data = json.load(f)
                for v in data.values():
                    obj = BaseModel(**v)
                    self.new(obj)
        except:
            pass
