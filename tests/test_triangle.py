from src.square import Square
import pytest


@pytest.mark.regression
@pytest.mark.parametrize(
    ("width", "area"),
    [
        pytest.param(3, 9, marks=pytest.mark.smoke, id="int"),
        pytest.param(3.5, 12.25, id="float"),
    ],
)
def test_square_area(width, area):
    figure = Square(width)

    assert figure.area == area, (
        f"Площадь равна {figure.area}, ожидаемый результат = {area}"
    )


@pytest.mark.regression
@pytest.mark.parametrize(
    ("width", "perimeter"),
    [
        pytest.param(3, 12, marks=pytest.mark.smoke, id="int"),
        pytest.param(3.3, 13.2, id="float"),
    ],
)
def test_square_perimeter(width, perimeter):
    figure = Square(width)

    assert figure.perimeter == perimeter, (
        f"Периметр равен {figure.perimeter}, ожидаемый результат {perimeter}"
    )



