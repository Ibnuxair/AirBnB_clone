#!/usr/bin/env python3

"""
This is a module that defines the base class.
"""


from datetime import datetime as time
from uuid import uuid4 as id


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initializes the attributes"""

        self.id = str(id())
        self.created_at = time.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returns the string representation of the object."""

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at. """
        self.updated_at = time.now()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance
        """

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict