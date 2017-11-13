#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Interger, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # DBStorage
    cities = relationship("City", backref="state")

    # FileStorage

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
