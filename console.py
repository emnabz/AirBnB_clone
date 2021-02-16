import cmd
from models import baseModel, place, state, city, Amenity, Review
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
