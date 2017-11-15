#!/usr/bin/python3
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """Representation of city """

    if os.getenv("HBNB_MYSQL_DB") == "db":  # if database

        __tablename__ = "cities"
        state_id = Column(String(60), nullable=False, ForeignKey="states.id")
        name = Column(String(128), nullable=False)

        places = relationship("Place", backref="cities")

    else:  # if filestorage
        state_id = ""
        name = ""

        def __init__(self, *args, **kwargs):
            """initializes city"""
            super().__init__(*args, **kwargs)
