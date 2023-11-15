#!/usr/bin/python3
""" this module is about class named square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class name square"""
    def __init__(self, size, x=0, y=0, id=None):
        """this function to define instance attribute """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this function to it returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
