from src.utils import Figure, Poligone


class Rectangle(Poligone, Figure):
    @property
    def perimeter(self):
        return round(((self.width + self.height) * 2), 2)

    @property
    def area(self):
        return round((self.width * self.height), 2)
