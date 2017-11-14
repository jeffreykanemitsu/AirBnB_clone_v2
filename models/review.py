#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """Representation of Review """
    if:
        __tablename__ = 'reviews'
        place_id = Column(String(60), nullable=False, ForeignKey('places.id')
        user_id = Column(String(60), nullable=False, ForeignKey('users.id')
        text = Column(String(1024), nullable=False)
    else:    
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
