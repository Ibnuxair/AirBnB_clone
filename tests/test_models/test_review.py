#!/usr/bin/env python3

"""
This module defines a class named TestReview.
"""


import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """ Test class for Review """

    def test_attributes(self):
        """ Test review attributes """

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
