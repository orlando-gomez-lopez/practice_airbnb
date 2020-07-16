#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """Class with test cases for the Review class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = Review()
        b1.place_id = "1"
        b1.user_id = "1"
        b1.text = "hello"
        self.assertAlmostEqual(b1.place_id, "1")
        self.assertAlmostEqual(b1.user_id, "1")
        self.assertAlmostEqual(b1.text, "hello")
