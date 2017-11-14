#!/usr/bin/python
""" holds class User"""
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """Representation of a user """
    if:
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', cascade='all, delete', backref='user')
        reviews = relationship('Place', cascale='all, delete', backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
