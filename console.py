#!/usr/bin/python3
"""
Module for the console
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """this is a simple command line interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self, arg):
        """
        a help command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        signal to exit the program
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()i
