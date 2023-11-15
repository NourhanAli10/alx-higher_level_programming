#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test new square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test new square with all attrs """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

