#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel, Base
from .city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    stored = os.environ.get('HBNB_TYPE_STORAGE')
    if stored == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan',
                              backref='state')
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            cities = []
            all_cities = storage.all(City)
            for key, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    cities.append(city_obj)
            return cities
