#!/usr/bin/env python3
""" console """

import cmd
from models.base_model import BaseModel
from shlex import split
import models
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
class_models = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                "City": City, "Place": Place, "Review": Review, "State": State}


class HBNBCommand(cmd.Cmd):
    """HBNH console"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_quit(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """Does nothing"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_models:
            instance = class_models[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints instance's string representation based on the class name and id
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_models:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_models:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, name=""):
        """ prints string repr. of all instances based on class name\n """
        store = storage.all()
        count = 0
        if name:
            if name not in class_models:
                for k, v in store.items():
                    if name in k:
                        print(v)
                        count += 1
                if count == 0:
                        print("[]")
                else:
                    print("** class doesn't exist **")
            else:
                for k, v in store.items():
                    print(v)

    def do_update(self, args):
        """ updates instance based on class name+id by adding/updating attr """
        args = args.split()
        store = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in class_models:
            print("** class doesn't exist **")
            return
        for k, v in store.items():
            if args[3].startswith('"') and args[3].endswith('"'):
                args[3] = args[3][1:-1]
            instance_key = args[0] + "." + args[1]
            if k == instance_key:
                setattr(v, args[2], args[3])
                storage.save()
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
