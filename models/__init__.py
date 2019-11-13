#!/usr/bin/python3
"""Initialize the models"""

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User,
           "BaseModel": BaseModel}


storage = FileStorage()
storage.reload()

