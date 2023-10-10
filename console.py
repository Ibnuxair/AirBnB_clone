#!/usr/bin/python3
""" This is the main/console def 4 de airbnb project """
import cmd, sys


class AirBnBConsole(cmd.Cmd):
    """ This is the class defination 4 cmd """

    prompt = ">>> "

if __name__ == "__main__":
    AirBnBConsole().cmdloop()