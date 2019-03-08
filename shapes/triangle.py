"""
Author: Nick Russo
File: circle.py
Purpose: Defines a Circle object, inherited from the abstract class Shape.
"""

from math import pi
from math import sqrt
from shapes.shape import Shape

class Triangle(Shape):
    """
    Represents a equilateral, and contains only a side value
    and number of decimal places to use when computing values.
    """
    decimal_places = 2

    def __init__(self, length):
        """
        Create the triangle by storing the length of one side.
        """
        self.length = length

    def area(self):
        """
        Compute the area using the formula area = (sqrt 3 / 4 ) x length ** 2
        """
        return round(( (sqrt(3) / 4) * self.length ** 2), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter is three time the length
        """
        return round (self.length * 3, self.decimal_places)
