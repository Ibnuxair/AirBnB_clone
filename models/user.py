#!/usr/bin/env python3

"""
This module define a class named User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    test_name = ""
    
    def __init__(self, *args, **kwargs):
        """ Initializes the attributes."""

        super().__init__(*args, **kwargs)

    def __str__(self):
        """ Returns the string representation of the object."""

        obj_dict = {k: v for k, v in self.__dict__.items() if v}
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, obj_dict)
