#!/usr/bin/python3
"""
This is the "console" module.
This module provides a simple command line interpreter to interact
with the application.
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Class for the HBNB command line interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        End of file command to exit the program.
        """
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args.split()[0]
            if class_name not in ['BaseModel', 'User', 'State', 'City',
                                  'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
            else:
                new_instance = eval(class_name + "()")
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if class_name not in ['BaseModel', 'User', 'State', 'City',
                                  'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                instance = models.storage.all()
                key = class_name + "." + instance_id
                if key not in instance:
                    print("** no instance found **")
                else:
                    print(instance[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            args = args.split()
            class_name = args[0]
            if class_name not in ['BaseModel', 'User', 'State', 'City',
                                  'Amenity', 'Place', 'Review']:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
               


if __name__ == '__main__':
    HBNBCommand().cmdloop()
