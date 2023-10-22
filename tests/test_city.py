#!/usr/bin/env python3

"""
This module defines a class named TestCity.
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Test class for City """

    def test_attributes(self):
        """ Test city attributes """

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
