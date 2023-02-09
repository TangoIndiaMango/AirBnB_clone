from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get('id', str(uuid4()))
            created_at = kwargs.get('created_at')
            self.created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f") if created_at else datetime.now()
            updated_at = kwargs.get('updated_at')
            self.updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f") if updated_at else datetime.now()
            for key, value in kwargs.items():
                if key not in ['id', 'created_at', 'updated_at', '__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        change_dict = self.__dict__.copy()
        change_dict['__class__'] = self.__class__.__name__
        change_dict['created_at'] = self.created_at.isoformat()
        change_dict['updated_at'] = self.updated_at.isoformat()
        return change_dict
