#!/usr/bin/env python3

"""
This module defines a class named TestAmenity.
"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test class for Amenity """

    def test_attributes(self):
        """ Test amenity attributes """

        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
