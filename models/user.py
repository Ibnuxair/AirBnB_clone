#!/usr/bin/env python3

"""
This module define a class named User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """ Initializes the attributes."""

        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    @classmethod
    def all(cls):
        """Returns a list of all instances of the User class."""

        return [obj for obj in storage.all().values() if isinstance(obj, cls)]

    def __str__(self):
        """ Returns the string representation of the object."""

        obj_dict = {k: v for k, v in self.__dict__.items() if v}

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, obj_dict)
