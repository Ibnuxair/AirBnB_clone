#!/usr/bin/env python3

"""
This module defines a class named TestFileStorage
"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ Create a fresh instance of FileStorage for each test. """

        self.storage = FileStorage()

        # Create a temporary file path for testing
        self.test_file_path = "test_file.json"

    def tearDown(self):
        # Remove the temporary file after testing
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

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

    def test_save_json_file(self):
        """ Test saving JSON data to the file. """

        # Create a sample dictionary with objects
        sample_dict = {
            'obj1': {'key1': 'val1'},
            'obj2': {'key2': 'val2'}
        }
        self.storage.__objects = sample_dict
        self.storage.save()

    def test_file_path_exists(self):
        """ Test if __file_path attribute exists in FileStorage. """

        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))

    def test_objects_attribute_ok(self):
        """ Test if __objects attribute is present and correct. """

        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_all_method_non_empty(self):
        """ Test the all() method with a non-empty dictionary. """

        # Assuming there is at least one object in storage
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertNotEqual(all_objects, {})
        self.assertIn(obj, all_objects.values())

    def test_new_method_adds_object(self):
        """ Test adding a new object to __objects dictionary using new(). """

        # Assuming there is a sample object to add
        obj = BaseModel()
        self.storage.new(obj)
        objects_dict = self.storage.all()
        self.assertIn(obj, objects_dict.values())

    def test_save_method_creates_file(self):
        """ Test saving JSON data to the file creates the file. """

        # Assuming there is at least one object in storage
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_method_restores_objects(self):
        """ Test reload method restores objects from file. """

        # Assuming there is a sample object in storage
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Load initial state
        initial_objects = self.storage.all().copy()

        # Reload storage
        self.storage.reload()

        # Check if the initial state is restored after reloading
        self.assertEqual(self.storage.all(), initial_objects)


    if __name__ == '__main__':
        unittest.main()
