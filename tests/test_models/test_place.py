#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class with test cases for the Place class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = Place()
        self.assertAlmostEqual(b1.number_rooms, 0)
