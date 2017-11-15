#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """Representation of state """

    # DBStorage
    if os.getenv("HBNB_MYSQL_DB") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else: # FileStorage
        @property
        def cities(self):
            """getter that returns list of city inst with state_id == State.id"""
            city_list = []
            for inst in models.storage.all(City).values():
                if inst.state_id == self.id:
                    city_list.append(inst)
            return city_list

        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)
