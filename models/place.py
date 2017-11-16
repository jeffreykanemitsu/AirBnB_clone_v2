#!/usr/bin/python3
""" holds class Place"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
import models

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Representation of Place """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """
            getter that returns list of reviews with place_id == Place.id
            """
            review_list = []
            for inst in models.storage.all(Reviews).values():
                if inst.place_id == self.id:
                    review_list.append(inst)
            return review_list

        @property
        def amenities(self):
            """
            getter that returns list of Amenity with place_id == Place.id
            """
            amenity_list = []
            for inst in models.storage.all(Amenity).values():
                if inst.place_id == self.id:
                    amenity_list.append(inst)
            return amenity_list

        def __init__(self, *args, **kwargs):
            """initializes Place"""
            super().__init__(*args, **kwargs)
