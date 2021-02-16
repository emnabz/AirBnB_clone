""" console"""
import cmd
from models import storage, class_models
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True
    
    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing
        """
        pass

    def do_create(self, class_model):
        """
        creates a new instance
        """
        if class_model in class_models:
            new_object = class_models[class_model] ()
            new_object.save()
            print ("new_object.id")
        elif len(class_model) == 0:
            print ("** class name missing **")
        else:
            print ("**class doesn't exist **")

    def do_show(self, args):
        store = storage.all()
        args = [x.strip() for x in args.split()]
        """
        prints the string representation of an instance
        """
    if len(args) == 2:
        if args[0] not in class_models:
            print ("** class doesn't exist **")
        else:
            instance_key = args[0] + '.' + arg[1]
            try:
                print (store[instance_key])
            except:
                print ("** no instance found **")
                
        if len(args) == 1:
            print("** instance id is missing **")            
            else:
                print ("** class name missing **") 
    
    def do_destroy(self,args):
        """ deletes instance based on class name+id """
        store = storage.all()
        args = [x.strip() for x in args.split()]
        if len(args) == 2:
            if args[0] not in class_models:
                print ("** class doesn't exist **")
                else:
                    instance_key = args[0] + '.' + args[1]
                try:
                    del (store[instance_key])
                except:
                    print ("** no instace found **")
        if len(args) == 1:
            print ("** instance id is missing **")                    
            else:
                print("** class name missing **")

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
    console = HBNBCommand()
    console.prompt = ' (hbnb) '
    console.cmdloop()
