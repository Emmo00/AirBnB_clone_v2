#!/usr/bin/python3
""" City Module for HBNB project """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models import state


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    stored = os.environ.get('HBNB_TYPE_STORAGE')
    if stored == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete-orphan', backref='cities')
    else:
        state_id = ""
        name = ""
