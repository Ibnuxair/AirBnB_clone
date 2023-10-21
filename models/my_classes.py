#!/usr/bin/env python3

"""
This module defines my classes.
"""


from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# Create a dictionary to map class names to their corresponding classes
my_classes = {
    'BaseModel': BaseModel,
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
    'User': User
}
