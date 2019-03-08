"""
Author: Nick Russo, Amended SimonG
File: triangle_test.py
Purpose: Unit tests for the triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle

class TriangleTest(TestCase):
    """
    Defines a test case for the triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.length5 = Triangle(5)
        self.length8 = Triangle(8)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.length5.area(), 10.83)
        self.assertEqual(self.length8.area(), 27.71)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.length5.perimeter(), 15)
        self.assertEqual(self.length8.perimeter(), 24)
