#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class City(BaseModel, Base):
    """Representation of city """
    if os.getenv("HBNB_MYSQL_DB") == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
