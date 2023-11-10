#!/usr/bin/env python3

"""
This module defines a class named HBNBCommand.
"""


import cmd
import sys
from models.my_classes import my_classes
from models.__init__ import storage


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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it and prints the id"""

        if not arg:
            print("** class name missing **")
        else:
            class_name = arg
            if class_name not in my_classes:
                print("** class doesn't exist **")
            else:
                obj = my_classes[class_name]()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """
        Prints the str rep. of an instance based on the class name and id.
        """

        # Split the arguments
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in my_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                k = "{}.{}".format(class_name, obj_id)
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[k]
                    print(obj)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id. """

        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in my_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                k = "{}.{}".format(class_name, obj_id)
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    storage.all().pop(k)
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string repr. of instances based or not on the class name.
        """

        all_objects = storage.all()

        if not arg:
            instances = [
                "{}".format(str(obj))
                for k, obj in all_objects.items()
            ]
            print(instances)
        elif arg not in my_classes:
            print("** class doesn't exist **")
        else:
            instances = [
                "{}".format(str(obj))
                for k, obj in all_objects.items()
                if k.split(".")[0] == arg
            ]
            print(instances)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """

        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if class_name not in my_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                k = "{}.{}".format(class_name, obj_id)
                if k not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    # Get the instance from storage
                    obj = storage.all()[k]
                    attribute_name = args[2]
                    attribute_value = args[3]

                    # Check if obj is a dictionary (dict)
                    if isinstance(obj, dict):
                        # Update the dict key with the new attribute value
                        obj[attribute_name] = attribute_value
                    else:
                        # Get the attribute's data type from the class
                        attribute_type = type(getattr(obj, attribute_name))

                        # Cast the attribute value to the correct data type
                        if attribute_type is int:
                            attribute_value = int(attribute_value)
                        elif attribute_type is float:
                            attribute_value = float(attribute_value)
                        elif attribute_type is str:
                            attribute_value = str(attribute_value)

                        # Update the attribute and save the instance
                        setattr(obj, attribute_name, attribute_value)

                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
