#!/usr/bin/python3
""" this module is about class named square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """this class name square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        
    
    
    
