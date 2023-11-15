#!/usr/bin/python3
'''Module for rectangle unit tests.'''
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO




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
        
    # display rectangale   
    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)
            
    def test_str(self):
        obj = Rectangle(4, 6, 2, 1, 2)
        res = "[Rectangle] (2) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(obj)
            self.assertEqual(str_out.getvalue(), res)
            
    def test_display_with_x_y(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)
        
        
        
    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89,2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3,4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        
        
    def test_update_with_positional_args(self):
        my_rectangle = Rectangle(10, 20)
        my_rectangle.update(30, 40)
        self.assertEqual(my_rectangle.width, 30)
        self.assertEqual(my_rectangle.height, 40)

    def test_update_with_keyword_args(self):
        my_rectangle = Rectangle(10, 20)
        my_rectangle.update(50, 60)
        self.assertEqual(my_rectangle.width, 50)
        self.assertEqual(my_rectangle.height, 60)

    def test_update_with_mixed_args(self):
        my_rectangle = Rectangle(10, 20)
        my_rectangle.update(30, 50)
        self.assertEqual(my_rectangle.width, 30)
        self.assertEqual(my_rectangle.height, 50)

    def test_update_with_empty_args(self):
        my_rectangle = Rectangle(10, 20)
        my_rectangle.update()
        self.assertEqual(my_rectangle.width, 10)
        self.assertEqual(my_rectangle.height, 20)

    def test_update_with_extra_positional_args(self):
        my_rectangle = Rectangle(10, 20)
        my_rectangle.update(30, 40, 50)
        self.assertEqual(my_rectangle.width, 30)
        self.assertEqual(my_rectangle.height, 40)
        

if __name__ == '__main__':
    unittest.main()
