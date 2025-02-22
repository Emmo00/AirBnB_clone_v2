#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', ForeignKey('amenities.id'),
                             nullable=False, primary_key=True),
                      mysql_collate='latin1_swedish_ci')


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review',
                           cascade='all, delete-orphan', backref='place')
    amenities = relationship('Amenity',
                             secondary=place_amenity, viewonly=False,
                             back_populates='place_amenities')

    @property
    def amenity_ids(self):
        list_ids = []
        for amenity in self.amenities:
            list_ids.append(amenity.id)
        return list_ids
