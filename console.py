import cmd
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

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
