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
        self.assertEqual(obj.id, 3)
        
    def test__with_width_height(self):
        obj = Rectangle(width=5, height=10)
        self.assertEqual(obj.x, 0)
        
    def test_errors(self):
        obj = Rectangle("5", 10)
        self.assertRaises(TypeError)
    
    def test_errors(self):
        obj = Rectangle(5, "10")
        self.assertRaises(TypeError)
        
    def test_errors(self):
        obj = Rectangle(1, 10)
        self.assertRaises(ValueError)
        
    def test_area(self):
        obj = Rectangle(2, 10)
        self.assertEqual(obj.area(), 20)
    
    def test_area(self):
        obj = Rectangle(2, 10, 1 , 4)
        self.assertEqual(obj.area(), 20)
        
    
    
