#!/usr/bin/python3
"""unittests for this project"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Class with test cases for the HBNBCommand class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = HBNBCommand()
        self.assertAlmostEqual(b1.prompt, "(hbnb) ")
