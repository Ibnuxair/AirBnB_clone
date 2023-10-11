#!/usr/bin/python3
""" This is the class defination 4 de airbnb project """
import cmd, sys
from models import BaseModel


class AirBnBConsole(cmd.Cmd):
    """ This is the class representation 4 cmd """

    prompt = "(hbnb) "

if __name__ == "__main__":
    AirBnBConsole().cmdloop()