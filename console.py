#!/usr/bin/env python3
""" console """

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
