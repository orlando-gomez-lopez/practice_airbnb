#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class with test cases for the Amenity class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = Amenity()
        b1.name = "fireplace"        
        self.assertAlmostEqual(b1.name, "fireplace")
