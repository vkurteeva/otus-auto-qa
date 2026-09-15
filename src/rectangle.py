from utils import Figure, Poligone


class Rectangle(Poligone, Figure):
    @property
    def perimeter(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height
