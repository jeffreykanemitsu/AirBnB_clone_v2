#!/usr/bin/python3
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """Representation of city """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":  # if database

        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)

        #places = relationship("Place", cascade='all, delete',  backref="cities")

    else:  # if filestorage
        state_id = ""
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes city"""
            super().__init__(*args, **kwargs)
