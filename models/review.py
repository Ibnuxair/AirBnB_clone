#!/usr/bin/env python3

"""
This module defines a class named Review.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """

    place_id = ""
    user_id = ""
    text = ""
