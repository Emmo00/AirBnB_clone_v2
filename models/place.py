#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


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
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade='all, delete-orphan', backref='place')
    else:
        @property
        def reviews(self):
            reviews = []
            all_reviews = storage.all(Review)
            for key, review_obj in all_reviews.items():
                if review_obj.place_id == self.id:
                    reviews.append(review_obj)
            return reviews
