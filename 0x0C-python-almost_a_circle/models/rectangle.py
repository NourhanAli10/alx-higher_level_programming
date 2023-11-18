#!/usr/bin/python3
""" this module is about class named base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that ingerit from base"""
    # task 2,3
    def __init__(self, width, height, x=0, y=0, id=None):
        """this function to define instance attribute """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # task 4
    def area(self):
        """this function to calculate rectangle area"""
        return self.__width * self.__height

    # task 5,7
    def display(self):
        """this function to that prints in stdout
        the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="\n")

    # task 6
    def __str__(self):
        """this function to it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    # task 8 & 9
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args (int): arguments to send a non-keyworded variable
                length argument list to the function
            kwargs (dict): keyworded variable length of arguments
        """
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]

    # task 13
    def to_dictionary(self):
        """function returns the dictionary representation of a Rectangle"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
