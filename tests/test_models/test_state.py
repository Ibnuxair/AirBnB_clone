#!/usr/bin/env python3

"""
This module defines a class named TestState.
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test class for State """

    def test_attributes(self):
        """ Test state attributes """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
