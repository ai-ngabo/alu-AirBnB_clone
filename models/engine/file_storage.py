#!/usr/bin/python3
"""
This module defines a FileStorage class that stores
and retrieves objects to and from a JSON file.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A file storage system for storing and retrieving objects.
    """
    class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review

            }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently stored.

        Returns:
            dict: A dictionary of all objects currently stored.
        """
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage"""
        class_name = obj.__class__.__name__  # Get class name from object
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj  # Store the actual object, not undefined 'value'
    def save(self):
        """
        Saves the objects in the storage to a JSON file.
        """
        obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file, indent=2)

    def reload(self):
        """
        Reloads the objects from the JSON file into the storage.
        """
        if os.path.exists(self.__file_path):

            with open(self.__file_path, 'r') as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name = value.pop['__class__', None]

                        if class_name in self.class_dict:
                            self.__objects[key] = self.class_dict[class_name](**value)  # Ensure value is passed correctly

                except json.JSONDecodeError:
                    pass

        else:
            pass
