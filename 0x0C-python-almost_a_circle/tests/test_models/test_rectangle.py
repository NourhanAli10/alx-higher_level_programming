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
    #task 2

    def test_constructor_with_id(self):
        obj = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(obj.width, 5)
        
    def test_constructor_without_id(self):
        obj = Rectangle(width=5, height=10, x=2, y=3)
        self.assertEqual(obj.id, 3)
        
    def test__with_width_height(self):
        obj = Rectangle(width=5, height=10)
        self.assertEqual(obj.x, 0)
    #task 3  
    def test_errors(self):
        obj = Rectangle("5", 10)
        self.assertRaises(TypeError)
    
    def test_errors(self):
        obj = Rectangle(5, "10")
        self.assertRaises(TypeError)
        
    def test_errors(self):
        obj = Rectangle(1, 10)
        self.assertRaises(ValueError)
    #task 4   
    def test_area(self):
        obj = Rectangle(2, 10)
        self.assertEqual(obj.area(), 20)
    
    def test_area(self):
        obj = Rectangle(2, 10, 1 , 4)
        self.assertEqual(obj.area(), 20)
        
    # task 5   
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
    #task 6      
    def test_str(self):
        obj = Rectangle(4, 6, 2, 1, 2)
        res = "[Rectangle] (2) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(obj)
            self.assertEqual(str_out.getvalue(), res)
    # task 7       
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
        
        
    #task 8  
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
        
    #task 9   
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
        
    #task 13    
    def test_M_to_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.width = 30
        r.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(r.to_dictionary(), d)

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        
        

if __name__ == '__main__':
    unittest.main()
