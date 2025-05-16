#!/usr/bin/python3
"""
    Module to present BaseModel class that defines
    all common attributes.methods for model classes
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items(): 
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4()) # Generate a unique Id
            self.created_at = datetime.now() # current timestamp
            self.updated_at = datetime.now() # Current timestamp
            models.storage.new(self) # Add object to storage

    def save(self):
        self.updated_at = datetimr.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            obj_dict[key] = value

        return obj_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
