from src.utils import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return round((2 * math.pi * self.radius), 2)

    @property
    def area(self):
        return round((math.pi * self.radius**2), 2)
