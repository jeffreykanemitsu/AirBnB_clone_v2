#!/usr/bin/python3
"""Engine for Database Storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__engine = None
__session = None

def __init__(self):
    """ creates connection to db"""
    dilect = 'mysql'
    driver = 'mysqldb'
    usr = 'hbnb_dev'
    pwd = 'hbnb_dev_pwd'
    db = 'hbnb_dev_db'
    self.__engine = create_engine(dilect+driver+'://'+usr+':'+pwd+'@localhost '+db)

def all(self, cls=None):
    """query on current db"""
    if cls:
        result = self.__session.query(cls).all()
    else:
        result = self.__session.query(User).all()
        result += self.__session.query(State).all()
        result += self.__session.query(City).all()
        result += self.__session.query(Amenity).all()
        result += self.__session.query(Place).all()
        result += self.__session.query(Review).all()




