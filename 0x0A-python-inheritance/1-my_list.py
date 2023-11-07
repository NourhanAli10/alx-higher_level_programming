#!/usr/bin/python3
"""
This module provides a single function 'lookup' that
can be used to retrieve a list of attributes and methods
of any Python object.
"""

class MyList(list):
    """Class with method print_sorted"""
    def print_sorted(self):
        """Methot that sorted a list"""        
        print(sorted(list(self)))
