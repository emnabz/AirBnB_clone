import cmd
from baseModel import baseModel


class HBNBcommand(cmd.Cmd):
    
    intro = 'Welcome to the hbnb shell. Type help or ? to list commands.
    prompt = '(hbnb)'
    
# ----- basic turtle commands -----
def do_quit(self, arg):
    'Quit command to exit the program\n'
    return True

def do_EOF(self,arg):
    'Quit command to exit the program\n'
    return True

def emptyline(self):
    pass
