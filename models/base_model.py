#!/usr/bin/python3
""" This is the BaseModel class defination 4 de AirBnB project """
import models, sys
from datetime import datetime as time
from uuid import uuid4 as id

class BaseModel:
    """ This is the class representation 4 de AirBnB project"""
    def __init__(self, *args, **kwargs) -> None:
        """ This is the BaseModel class initializatio
        Atributes:
            *args (args): Undefined number of args
            **kwargs (dic): Undeifned number of keyword args
        """
        self.id = str(id)
        self.created_at = time.today()
        self.updated_at = time.today()

    def __str__(self):
        """This is the defination printing Basemodel as str """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at == time.today()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        returning_dic = self.__dict__.copy()
        returning_dic["created_at"] = str(self.created_at.isoformat())
        returning_dic["updated_at"] = str(self.updated_at.isoformat())
        returning_dic["__class__"] = str(self.__class__.__name__)
        return returning_dic