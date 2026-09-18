from utils import Figure, Poligone


class Square(Figure, Poligone):
    def __init__(self, width):
        super().__init__(width)

    @property
    def perimeter(self):
        return self.width * 4

    @property
    def area(self):
        return self.width**2
