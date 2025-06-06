import uuid
from datetime import datetime
import models
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'uodated_at']:
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
        
 
    def to_dict(self):
        
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        if isinstance(self.updated_at, str):
            instance_dict["updated_at"] = self.updated_at
        else:
            instance_dict["updated_at"] = self.updated_at.isoformat()

        for key, value in self.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                instance_dict[key] = value
        return instance_dict
