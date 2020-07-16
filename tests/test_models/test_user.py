#!/usr/bin/python3
"""unittests for this project"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Class with test cases for the User class"""

    def test_attrib(self):
        """Test attribute assignment"""
        b1 = User()
        b1.password = "123456789"        
        self.assertAlmostEqual(b1.password, "123456789")

    def test_save(self):
        """Test validation updated_at"""
        b1 = User()
        up1 = b1.updated_at
        b1.save()
        up2 = b1.updated_at
        b1.save()
        self.assertNotEqual(up1, up2)

    def test_instance(self):
        """Test validation instance"""
        b1 = User()
        self.assertIsInstance(b1, User)

    def test_access(self):
        """Test access file"""
        access = os.access("models/user.py", os.R_OK)
        self.assertTrue(access, "Read permissions")
