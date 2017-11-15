#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """Representation of state """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    enviroment = {
                    'user': HBNB_MYSQL_USER, 'password': HBNB_MYSQL_PWD,
                    'host': HBNB_MYSQL_HOST, 'database': HBNB_MYSQL_DB
                }
    for var, env in enviroment.items():
        enviroment[var] = os.getenv(env, None)

    # DBStorage
    if enviroment['database']:
        cities = relationship("City", backref="state")
    else:


    # FileStorage

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
