#!/usr/bin/python3
""" model for unittest base"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ class to test """
    def test_constructor_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
    




if __name__ == '__main__':
    unittest.main()
