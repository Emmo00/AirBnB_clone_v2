#!/usr/bin/python3
"""db_storage module
implements the DBStorage class
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB')
            ), pool_pre_ping=True)
        if os.environ.get('HBNB_ENV'):
            # drop all tables

    def all(self, cls=None):
        if cls is not None:
            instances = self.__session.query(cls).all()
        else:
            instances = self.__session.query(User, State, City, Amenity, Place, Review).all()
        all_instances = {}
        for instance in instances:
            all_instances['{}.{}'.format(instance.__class__.__name__, instance.id)] = instance
        return all_instances

    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj == None:
            return
        self.__session.delete(obj)

    def reload(self):
        Base.metedata.create_all(engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
