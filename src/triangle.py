from typing import Union
from utils import Figure, Poligone


# class Triangle(Figure):
#     def __init__(self, base: int, height: int, leg_a: int, leg_b: int):
#         self.base = base
#         self.height = height
#         self.leg_a = leg_a
#         self.leg_b = leg_b
#
#     @property
#     def perimeter(self):
#         return self.base + self.leg_b + self.leg_a
#
#     @property
#     def area(self):
#         return 0.5 * self.base * self.height


class Triangle(Poligone, Figure):
    def __init__(
        self, width, height, leg_a: Union[int, float], leg_b: Union[int, float]
    ):

        super().__init__(width, height, leg_a, leg_b)
        self.leg_a = leg_a
        self.leg_b = leg_b
        self.base = self.width

    @property
    def perimeter(self):
        return self.base + self.leg_b + self.leg_a

    @property
    def area(self):
        return 0.5 * self.base * self.height


t = Triangle(1, 5, 3, 3)
print(t.perimeter)
print(t.area)
