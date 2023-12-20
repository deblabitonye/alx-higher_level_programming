#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass.

        Args:
        radius (int or float): The radius of the MagicClass.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculate the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
