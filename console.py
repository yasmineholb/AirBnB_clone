#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ cmd class """
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]
    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

    def main():
        """ main function """
        do_EOF(self, arg)
        do_quit(self, arg)
        emptyline(self)

    def default(self, arg):
        if '.' not in arg:
            print("*** Unknown syntax: ", arg)
            return
        y = arg.split('.')
        if y[0] == "":
            print("** class name missing **")
            return
        if y[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if y[1] == "all()":
            self.fn_all(y[0])
        elif y[1] == "count()":
            self.fn_count(y[0])
        elif y[1][0:5] == "show(" and y[1][-1] == ")":
            self.fn_show(y[0], y[1])
        elif y[1][0:8] == "destroy(" and y[1][-1] == ")":
            self.fn_destroy(y[0], y[1])
        elif y[1][0:7] == "update(" and y[1][-1] == ")":
            self.fn_update(y[0], y[1])
        else:
            print("*** Unknown syntax: ", arg)

    def fn_all(self, y0):
        """
        function <class>.all()
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        print("[", end="")
        c = 0
        for v in objects.values():
            if v.__class__.__name__ == y0:
                if c != 0:
                    print(", ", end="")
                c += 1
                print(v, end="")
        print("]")

    def fn_count(self, y0):
        """ retrieve the number of instances of a class """
        objects = storage.all()
        c = 0
        for v in objects.values():
            if v.__class__.__name__ == y0:
                c += 1
        print(c)

    def fn_show(self, y0, y1):
        """ retrieve an instance based on its ID """
        m = y1.split('(')
        d = m[1].split(')')
        my_id = d[0]
        if my_id == "":
            print("** instance id missing **")
            return
        objects = storage.all()
        for v in objects.values():
            if my_id == v.id and v.__class__.__name__ == y0:
                print(v)
                return
        print("** no instance found **")

    def fn_destroy(self, y0, y1):
        """ destroys an instance based on his ID """
        m = y1.split('(')
        d = m[1].split(')')
        my_id = d[0]
        if my_id == "":
            print("** instance id missing **")
            return
        key = y0 + "." + my_id
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def fn_update(self, y0, y1):
        """ update an instance """
        m = y1.split('(')
        d = m[1].split(')')
        param = d[0]
        n = param.split(', ')
        if n[0] == "":
            print("** instance id missing **")
            return
        key = y0 + "." + n[0]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(n) == 1 or n[1] == "":
            print("** attribute name missing **")
            return
        if n[1][0] == '{' and n[1][-1] == '}':
            self.fn_update2(n[1], objects[key])
            return
        if len(n) == 2 or n[2] == "":
            print("** value missing **")
            return
        attr = n[1]
        try:
            value = getattr(objects[key], attr)
            t = type(value)
            setattr(objects[key], attr, t(n[2]))
        except:
            setattr(objects[key], attr, n[2])
        storage.save()

    def fn_update2(self, d, obj):
        """ update attributes of an object given in a dictionary """
        dic = eval(d)
        for k, v in dic.items():
            try:
                value = getattr(obj, k)
                t = type(value)
                setattr(obj, k, t(v))
            except:
                setattr(obj, k, v)
            storage.save()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if arg == '':
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
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
            if x[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = x[0] + "." + x[1]
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
            if x[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                if len(x) == 1:
                    print("** instance id missing **")
                else:
                    key = x[0] + "." + x[1]
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
        if arg == '':
            objects = storage.all()
            l = []
            for v in objects.values():
                l.append(str(v))
            print(l)
        elif arg in HBNBCommand.classes:
            objects = storage.all()
            l = []
            for v in objects.values():
                if v.__class__.__name__ == arg:
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
        if y[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(y) == 1:
            print("** instance id missing **")
            return
        key = y[0] + "." + y[1]
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
