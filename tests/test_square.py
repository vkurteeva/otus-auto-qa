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
    act_area = round(figure.area, 2)

    assert act_area == area, (
        f"Площадь равна {act_area}, ожидаемый результат = {area}"
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
    act_perimeter = round(figure.perimeter, 2)

    assert act_perimeter == perimeter, (
        f"Периметр равен {act_perimeter}, ожидаемый результат {perimeter}"
    )



