#!/usr/bin/env python3

"""
This module defines a class named TestUserModel.
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUserModel(unittest.TestCase):
    """ A class that tests User Class."""

    def test_inheritance(self):
        """
        Test if User class inherits from BaseModel.
        """

        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
        Test if User has the expected public class attributes.
        """

        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_values(self):
        """
        Test if User attributes have the correct default values.
        """

        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
