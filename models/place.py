#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))


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
    amenity_ids = []

    stored = os.environ.get('HBNB_TYPE_STORAGE')
    if stored == 'db':
        reviews = relationship('Review',
                               cascade='all, delete-orphan', backref='place')
        amenities = relationship('Amenity',
                                 secondary=place_amenity, viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            reviews = []
            all_reviews = storage.all(Review)
            for key, review_obj in all_reviews.items():
                if review_obj.place_id == self.id:
                    reviews.append(review_obj)
            return reviews

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            amenities = []
            all_amenities = storage.all(Amenity)
            for key, amenity_obj in all_amenities.items():
                if amenity_obj.id in self.amenity_ids:
                    amenities.append(amenity_obj)
            return amenities

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
