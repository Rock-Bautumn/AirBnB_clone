#!/usr/bin/python3

"""
defining all common attributes/methods for other classes
"""
from datetime import datetime as dt
from uuid import uuid4
import models


class BaseModel:
    """
    Establish class basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel object
        """
        if len(args) > 0:
            raise SyntaxError("BaseModel.update does not support args,\
                use kwargs instead.")
        self.created_at = dt.now()
        self.updated_at = self.created_at
        self.id = str(uuid4())
        self.update(**kwargs)
        models.storage.new(self)

    def update(self, *args, **kwargs):
        """
        Update the BaseModel with new arbitrary properties
        """
        if len(args) > 0:
            raise SyntaxError("BaseModel.update does not support args, \
                use kwargs instead.")
        for i in kwargs:
            if i == "id":
                self.id = kwargs[i]
            if i == "created_at":
                newtime = kwargs[i]
                if type(newtime) == str:
                    try:
                        dto = dt.fromisoformat(newtime)
                    except ValueError:
                        raise ValueError("value for created_at must be\
                            a valid ISO format time string")
                elif newtime.__class__.__name__ == "datetime":
                    dto = dt.fromisoformat(dt.isoformat(newtime))
                else:
                    raise ValueError("value for created_at must be a\
                        valid ISO format time string")
                self.created_at = dto
            if i == "updated_at":
                newtime = kwargs[i]
                if type(newtime) == str:
                    try:
                        dto = dt.fromisoformat(newtime)
                    except ValueError:
                        raise ValueError("value for updated_at must be a\
                            valid ISO format time string")
                elif newtime.__class__.__name__ == "datetime":
                    dto = dt.fromisoformat(dt.isoformat(newtime))
                else:
                    raise ValueError("value for updated_at must be a\
                        valid ISO format time string")
                self.updated_at = dto

    def __str__(self):
        """
        This makes a pretty string representation of our BaseModel object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates public instance attribute updated_at w/ current time
        """
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns new_dict of all key/values
        converts info into human readable info
        """
        new_dict = self.__dict__.copy()
        d = {'created_at': dt.isoformat(self.created_at)}
        new_dict.update(d)
        d = {'updated_at': dt.isoformat(self.updated_at)}
        new_dict.update(d)
        d = {'__class__': self.__class__.__name__}
        new_dict.update(d)
        return new_dict
