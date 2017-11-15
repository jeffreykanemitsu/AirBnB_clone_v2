#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class Amenity(BaseModel, Base):
    """Representation of Amenity """

    if os.getenv("HBNB_MYSQL_DB") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
