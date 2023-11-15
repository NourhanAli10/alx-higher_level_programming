#!/usr/bin/python3
'''Module for rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    '''Tests the Rectangle class.'''

    def test_constructor_with_id(self):
        obj = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(obj.width, 5)
        
    def test_constructor_without_id(self):
        obj = Rectangle(width=5, height=10, x=2, y=3)
        self.assertEqual(obj.id, 2)
        
    def test__with_width_height(self):
        obj = Rectangle(width=5, height=10)
        self.assertEqual(obj.x, 0)
    
