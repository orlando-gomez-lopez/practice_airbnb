#!/usr/bin/python3
""" module point 5 file_storage """
import json
import models
from models import *


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}
    __count_user = 0
    __count_amenity = 0
    __count_city = 0
    __count_place = 0
    __count_review = 0
    __count_state = 0
    __count_base = 0

    def c_user(self):
        return self.__count_user

    def c_amenity(self):
        return self.__count_amenity

    def c_city(self):
        return self.__count_city

    def c_place(self):
        return self.__count_place

    def c_review(self):
        return self.__count_review

    def c_state(self):
        return self.__count_state

    def c_base(self):
        return self.__count_base

    def all(self):
        """all function"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        objName = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[objName] = obj
	
        if type(obj).__name__ == "User":
           FileStorage.__count_user = FileStorage.__count_user + 1
        
        if type(obj).__name__ == "Amenity":
           FileStorage.__count_amenity = FileStorage.__count_amenity + 1

        if type(obj).__name__ == "City":
           FileStorage.__count_city = FileStorage.__count_city + 1

        if type(obj).__name__ == "Place":
           FileStorage.__count_place = FileStorage.__count_place + 1

        if type(obj).__name__ == "Review":
           FileStorage.__count_review = FileStorage.__count_review + 1

        if type(obj).__name__ == "State":
           FileStorage.__count_state = FileStorage.__count_state + 1

        if type(obj).__name__ == "BaseModel":
           FileStorage.__count_base = FileStorage.__count_base + 1

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        n_dict = {}
        with open(self.__file_path, "w", encoding='utf-8') as f:
            for key, value in self.__objects.items():
                n_dict[key] = value.to_dict()
            json.dump(n_dict, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                o_dict = json.load(f)
                for key, value in o_dict.items():
                    cl = key.split(".")
                    value.pop("__class__")
                    if cl[0] == "BaseModel":
                        bmObj = BaseModel(**value)
                    if cl[0] == "User":
                        bmObj = User(**value)
                    if cl[0] == "State":
                        bmObj = State(**value)
                    if cl[0] == "City":
                        bmObj = City(**value)
                    if cl[0] == "Amenity":
                        bmObj = Amenity(**value)
                    if cl[0] == "Place":
                        bmObj = Place(**value)
                    if cl[0] == "Review":
                        bmObj = Review(**value)
                    self.new(bmObj)
        except:
            pass
