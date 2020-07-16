#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class with test cases for the City class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = City()
        b1.state_id = "1"
        b1.name = "Cali"
        self.assertAlmostEqual(b1.name, "Cali")
