#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def test_constructor_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
