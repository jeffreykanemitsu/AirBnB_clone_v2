#!/usr/bin/python3
"""
Test the database version of Place
"""
from os import environ
environ["HBNB_TYPE_STORAGE"] = "db"
from models import Place
from models.base_model import BaseModel
from datetime import datetime
import unittest
Place = place.Place


class TestPlace_db(unittest.TestCase):
    """Test the Place class with db storage"""

    attributes = {'name': "MyVilla"}

    row = Place(**attributes)

    def test_mysql_obj(self):
        """Test that instance ORM object"""
        self.assertTrue(hasattr(self.row, '_sa_instance_place'))

    def test_table_name(self):
        """Test that table name is places"""
        self.assertEqual(self.row.__tablename__, "places")

    def test_time_obj(self):
        """Test that created_at and updated_at is date and time object"""
        self.assertTrue(type(self.row.created_at), datetime)
        self.assertTrue(type(self.row.updated_at), datetime)
        self.assertEqual(type(self.row), Place)


    def test_isChild(self):
        """Test if instance is child of Place"""
        self.assertIsInstance(self.row, Place)

    def test_attributes(self):
        """Test for required attr for table places"""
        self.attributes.update({'id': None, 'cities': None})
        for attr in self.attributes.keys():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.row, attr))
