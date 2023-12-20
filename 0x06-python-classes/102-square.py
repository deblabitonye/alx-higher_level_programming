#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int or float): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
        value (int or float): The size to set.

        Raises:
        TypeError: If the size is not a number.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison based on the area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison based on the area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Less than or equal comparison based on the area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Greater than comparison based on the area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Greater than or equal comparison based on the area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
