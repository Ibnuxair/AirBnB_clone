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
