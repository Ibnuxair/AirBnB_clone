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
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """ Returns the string representation of the object."""

        attributes = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

        non_empty_attributes = {k: v for k, v in attributes.items() if v}

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, non_empty_attributes)
