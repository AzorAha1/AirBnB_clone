#!/usr/bin/python3

import json
import os

"""Define a class"""


class FileStorage:
    """
    a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        import models.base_model
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(file=FileStorage.__file_path, mode='w') as file:
            serialized = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, models.base_model.BaseModel):
                    serialized[key] = value.to_dict()
                else:
                    serialized[key] = value
            json.dump(serialized, file)

    def reload(self):
        """deserialization of the object file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(file=FileStorage.__file_path, mode='r') as file:
                for key, value in json.load(file).items():
                    nameofclass = value['__class__']
                    if nameofclass in self.classes():
                        theclass = self.classes()[nameofclass]
                        instance = theclass(**value)
                        FileStorage.__objects[key] = instance
        else:
            pass

    def classes(self):
        """Returns a dictionary of all classes in the console"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }
        return class_dict
