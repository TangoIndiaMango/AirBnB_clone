""" class FileStorage
serializes instances to a JSON file
and deserializes JSON file to instances """
import json
import os

class FileStorage:
""" construct """
__file_path = "file.json"
__objects = {}

    def all(self):
    """ returns a dictionary of all objects """
        return FileStorage.__objects

    def new(self, obj):
    """ adds a new object to the dictionary with the key being the class name and id of the object """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
    """ serializes the objects in the dictionary and saves it to a JSON file """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
    """ reloads the JSON file and updates the objects in the dictionary """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                data = json.load(fname)
                for key, val in data.items():
                    FileStorage.__objects[key] = eval(val['__class__'])(**val)
