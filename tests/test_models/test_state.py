#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Class with test cases for the State class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = State()
        b1.name = "Lousiana"        
        self.assertAlmostEqual(b1.name, "Lousiana")

    def test_instance(self):
        """Test instance"""
        b1 = State()
        self.assertIsInstance(b1, State)

    def test_update(self):
        """Test update"""
        b1 = State()
        self.assertEqual(b1.updated_at.strftime("%b %d %Y %H:%M"), datetime.datetime.now().strftime("%b %d %Y %H:%M"))
