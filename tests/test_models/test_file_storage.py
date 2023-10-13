#!/usr/bin/env python3

"""
This module defines a class named TestFileStorage
"""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ Create a fresh instance of FileStorage for each test. """

        self.storage = FileStorage()

    def test_to_json_string_with_objects(self):
        """ Test to_json_string with a dictionary containing objects. """

        sample_dict = {
            'obj1': {'key1': 'val1'},
            'obj2': {'key2': 'val2'}
        }
        json_str = self.storage.to_json_string(sample_dict)
        self.assertEqual(
            json_str, '{"obj1": {"key1": "val1"}, "obj2": {"key2": "val2"}}')

    def test_all_empty_dict(self):
        """ Test the all() method with an empty dictionary. """

        objects_dict = self.storage.all()
        self.assertNotEqual(objects_dict, {})

    def test_new_object_addition(self):
        """ Test adding a new object to __objects dictionary using new(). """

        # Create a sample object
        class SampleObject:
            def __init__(self, id):
                self.id = id
        obj = SampleObject('sample_id')
        self.storage.new(obj)
        objects_dict = self.storage.all()
        self.assertIn('SampleObject.sample_id', objects_dict)

    def test_save_json_file(self):
        """ Test saving JSON data to the file. """

        # Create a sample dictionary with objects
        sample_dict = {
            'obj1': {'key1': 'val1'},
            'obj2': {'key2': 'val2'}
        }
        self.storage.__objects = sample_dict
        self.storage.save()

    if __name__ == '__main__':
        unittest.main()
