#!/usr/bin/python3

"""
Console
Entry point for command interpreter
Should be able to make, edit, and delete things
"""
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import shlex
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classes_c = {'BaseModel': BaseModel, 'User': User, 'State': State,
             'City': City, 'Amenity': Amenity, 'Place': Place,
             'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    class created for command processor
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_quit(self, *line):
        """
        quits out of the program
        """
        quit()

    def do_EOF(self, *line):
        """
        End of file for the program
        """
        print()
        raise SystemExit

    def emptyline(self):
        """
        does nothing passes epty line
        """
        pass

    def do_create(self, line):
        """
        New instance of BaseModel
        """
        cmd_ln = self.parseline(line)[0]
        if len(line) == 0:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(cmd_ln)()
            new_object.save()
            print(new_object.id)

    def do_show(self, line):
        """
        Prints str of an instance based on class name and id
        """
        cmd_ln = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_ln is None:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            instance_class_name = models.storage.all().get(cmd_ln + '.' + arg)
            if instance_class_name is None:
                print("** no instance found **")
            else:
                print(instance_class_name)

    def do_destroy(self, line):
        """
        delete instance based on class name and id
        """
        cmd_ln = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_ln is None:
            print("** class name missing **")
        elif cmd_ln not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            temp = cmd_ln + '.' + arg
            instance_class_name = models.storage.all().get(temp)
            if instance_class_name is None:
                print("** no instance found **")
            else:
                del models.storage.all()[temp]
                models.storage.save()

    def do_all(self, line):
        """
        prints str of ALL instances if its class name or not
        """
        if line == "":
            for k in storage.all():
                print([str(storage.all()[k])])
        elif line not in classes_c.keys():
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if line == v.__class__.__name__:
                    print([str(storage.all()[k])])

    def do_update(self, line):
        """
        updates instance based on class name & id
        with adding or updating and attribute
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                # print(f"args3 is {args[3]}")
                # args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
