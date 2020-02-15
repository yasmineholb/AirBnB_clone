#!/usr/bin/python3
import cmd

import sys


class HBNBCommand(cmd.Cmd):
    """ """
    prompt = '(hbnb) '

    def main():
        do_EOF(self, arg)
        do_quit(self, arg)
        emptyline(self)

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        quit()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program

        """
        return True

    def emptyline(self):
        """ """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
