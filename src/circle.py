from utils import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius**2
