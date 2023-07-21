#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete-orphan',
                              backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            mine = []
            for city, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    mine.append(city_obj)
            return mine
