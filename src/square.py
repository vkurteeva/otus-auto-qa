from src.utils import Figure, Poligone


class Square(Poligone, Figure):
    def __init__(self, width):
        super().__init__(width, width)

    @property
    def perimeter(self):
        return round((self.width * 4), 2)

    @property
    def area(self):
        return round((self.width**2), 2)
