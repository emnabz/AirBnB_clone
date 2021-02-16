""" console"""
import cmd
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
        return False

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
        if name:
            if name not in class_models:
                print ("** class doesn't exist **")
                                     

if __name__ == '__main__':
    HBNBCommand().cmdloop()
