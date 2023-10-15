#!/usr/bin/env python3

"""
This module defines a class named HBNBCommand.
"""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ The entry point of the command interpreter. """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quit command to exit the program. """

        sys.exit()

    def do_EOF(self, args):
        """This EOF signal is to exit the program."""

        print("")
        sys.exit()

    def emptyline(self):
        """ Called when an empty line is entered. """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
