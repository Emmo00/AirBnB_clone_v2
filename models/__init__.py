#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from .state import State
from .user import User
from .amenity import Amenity
from .place import Place
from .review import Review
from .city import City
from .base_model import BaseModel

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
