from typing import Union
from src.utils import Figure, Poligone


class Triangle(Poligone, Figure):
    def __init__(
    self,
    base: Union[int, float],
    leg_a: Union[int, float, None] = None,
    leg_b: Union[int, float, None] = None,
    height: Union[int, float, None] = None
    ):
        if height is not None:
            Poligone.__init__(self, base, height, leg_a, leg_b)
        else:
            Poligone.__init__(self, base, 1, leg_a, leg_b)
        self.base = base
        self.leg_a = leg_a
        self.leg_b = leg_b
        self.height = height

    @property
    def perimeter(self):
        return round((self.base + self.leg_b + self.leg_a), 2)

    @property
    def area(self):
        return round((self.base * self.height * 0.5), 2)
