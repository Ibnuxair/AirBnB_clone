#!/usr/bin/env python3


"""
This module defines a class named TestBaseModel.
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test Base class. """

    def test_create_instance(self):
        """ Test creating instance. """

        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_create_instance_with_args(self):
        """ Test creating an instance with args. """

        args = ('arg1', 'arg2', 'arg3')
        instance = BaseModel(*args)
        self.assertIsInstance(instance, BaseModel)

    def test_create_instance_with_kwargs(self):
        """ Test creating an instance with kwargs. """

        kwargs = {
            'id': '123',
            'created_at': '2023-10-11T12:00:00.000000',
            'updated_at': '2023-10-11T12:00:00.000000',
            'custom_attribute': 'custom_value',
            '__class__': 'BaseModel'
        }
        instance = BaseModel(**kwargs)
        self.assertIsInstance(instance, BaseModel)
        self.assertEqual(instance.id, '123')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.custom_attribute, 'custom_value')

    def test_create_instance_with_args_and_kwargs(self):
        """ Test creating an instance with both args and kwargs. """

        args = ('arg1', 'arg2', 'arg3')
        kwargs = {
            'id': '123',
            'created_at': '2023-10-11T12:00:00.000000',
            'updated_at': '2023-10-11T12:00:00.000000',
            'custom_attribute': 'custom_value',
            '__class__': 'BaseModel'
        }
        instance = BaseModel(*args, **kwargs)
        self.assertIsInstance(instance, BaseModel)
        self.assertEqual(instance.id, '123')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.custom_attribute, 'custom_value')

    def test_id_is_valid_uuid(self):
        """ Test if the id is valid uuid4"""

        instance = BaseModel()
        try:
            uuid.UUID(instance.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID. ")

    def test_created_at_is_datetime(self):
        """ Test if created_at is an instance of datetime. """

        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """ Test if updated_at is an instance of datetime. """

        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_created_at_equals_updated_at_initially(self):
        """ Test if created_at and updated_at are equal initially. """

        instance = BaseModel()
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_save_updates_updated_at(self):
        """ Test if created_at and updated_at are not equal initially. """

        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_to_dict_structure(self):
        """ Test to dictionary. """

        instance = BaseModel()
        instance_dict = instance.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, instance_dict)

    def test_to_dict_date_format(self):
        """ Test the date/time farmat. """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(
            instance.created_at.strftime(date_format),
            instance_dict['created_at']
        )
        self.assertEqual(
            instance.updated_at.strftime(date_format),
            instance_dict['updated_at']
        )


if __name__ == '__main__':
    unittest.main()
