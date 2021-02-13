import cmd
from baseModel import baseModel, place, state, city, Amenity, Review
import models


class HBNBcommand(cmd.Cmd):
    
    prompt = '(hbnb)'
    
def do_quit(self, arg):
    """
    Quit command to eit the program
    """    
    return True

def do_EOF(self, arg):
    """
    EOF command to exit the program
    """
    return True

def emptyline(self):
    """
    """
    pass

