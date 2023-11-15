#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    
    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_constructor_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)
    
    def test_constructor_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_auto_assign_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)     
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
        
if __name__ == '__main__':
    unittest.main()
