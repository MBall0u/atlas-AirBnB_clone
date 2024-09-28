#!/usr/bin/python3
""" Console module """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class HBNBCommand(cmd.Cmd):
    """ HBNB console class """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
               'Place': Place, 'Review': Review, 'Amenity': Amenity}

    def preloop(self):
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, _):
        """ Exit the program """
        exit()

    def do_EOF(self, _):
        """ Handle EOF to exit program """
        print()
        exit()

    def emptyline(self):
        """ Ignore empty line input """
        pass

    def do_create(self, args):
        """ Create a new instance """
        if not args:
            print("** class name missing **")
            return
        cls_name = args.split()[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        attr_dict = self._parse_attributes(args.split()[1:])
        new_instance = self.classes[cls_name](**attr_dict)
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """ Show an instance by class name and id """
        cls_name, obj_id = self._parse_args(args)
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{obj_id}"
        obj = storage.all().get(key)
        print(obj if obj else "** no instance found **")

    def do_destroy(self, args):
        """ Destroy an instance by class name and id """
        cls_name, obj_id = self._parse_args(args)
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{obj_id}"
        if storage.all().pop(key, None):
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Show all instances or instances of a specific class """
        cls_name = args.split()[0] if args else None
        if cls_name and cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in storage.all().items()
               if not cls_name or k.startswith(cls_name)])

    def do_update(self, args):
        """ Update an instance by class name, id, attribute, and value """
        cls_name, obj_id, attr, val = self._parse_update_args(args)
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{obj_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        setattr(instance, attr, val)
        storage.save()

    def _parse_args(self, args):
        """ Helper to parse class name and id from args """
        parts = args.split()
        return (parts[0], parts[1] if len(parts) > 1 else None)

    def _parse_update_args(self, args):
        """ Helper to parse class name, id, attribute, and value for update """
        parts = args.split()
        return (parts[0], parts[1], parts[2], parts[3].strip("\""))

    def _parse_attributes(self, params):
        """ Helper to parse attributes for instance creation """
        attr_dict = {}
        for param in params:
            key, value = param.split('=', 1)
            value = value.strip('"').replace('_', ' ') if '"' in value else self._convert_type(value)
            attr_dict[key] = value
        return attr_dict

    def _convert_type(self, value):
        """ Helper to convert value to appropriate type """
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

if __name__ == "__main__":
    HBNBCommand().cmdloop()
