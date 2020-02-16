#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ cmd class """
    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

    def main():
        """ main function """
        do_EOF(self, arg)
        do_quit(self, arg)
        emptyline(self)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if arg == '':
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if arg == '':
            print("** class name missing **")
        else:
            x = arg.split()
            if x[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = "BaseModel." + x[1]
                    objects = storage.all()
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id and
        saves the change into the JSON file
        """
        if arg == '':
            print("** class name missing **")
        else:
            x = arg.split()
            if x[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = "BaseModel." + x[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()  
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if arg == '' or arg == "BaseModel":
            objects = storage.all()
            l = []
            for v in objects.values():
                l.append(str(v))
            print(l)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        and saves the change into the JSON file
        
        """
        if arg == '':
            print("** class name missing **")
            return
        y = arg.split()
        if y[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(y) == 1:
            print("** instance id missing **")
            return
        key = "BaseModel." + y[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(y) == 2:
            print("** attribute name missing **")
            return
        q = arg.split('"')
        if len(q) == 1:
            print("** value missing **")
            return
        attr = y[2]
        try:
            value = getattr(objects[key], attr)
            t = type(value)
            setattr(objects[key], attr, t(q[1]))
        except:
            setattr(objects[key], attr, q[1])
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """ do nothing when an empty line is entered """
        pass

    def postloop(self):
        """ postloop """
        if sys.stdin.isatty():
            print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
