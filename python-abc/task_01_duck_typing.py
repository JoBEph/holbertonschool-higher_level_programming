#!/usr/bin/env python3

"""import ABC and math"""

from abc import ABC, abstractmethod
import math
"""
define abstract class Shape with abstract methods area and perimeter
"""


class Shape(ABC):
    """Class Shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Define Circle frome Shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Define rectangle from Shape"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def shape_info(self):
    """accept all shape inside"""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
