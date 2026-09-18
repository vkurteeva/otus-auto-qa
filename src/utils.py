from typing import Union
from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if not (isinstance(other_figure, Figure)):
            raise TypeError(
                f"The other figure must be an instance of Figure - {other_figure}"
            )

        return self.area + other_figure.area


class Poligone:
    def __init__(self, width: Union[int, float], height: Union[int, float], *args):
        self.width = width
        self.height = height
        self.other_side = args

        if self.width <= 0 or self.height <= 0:
            raise ValueError("The side must be greater than 0")
