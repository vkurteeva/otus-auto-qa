from src.rectangle import Rectangle
import pytest


@pytest.mark.regression
@pytest.mark.parametrize(
    ("width", "height", "area"),
    [
        pytest.param(3, 5, 15, marks=pytest.mark.smoke, id="int"),
        pytest.param(3.5, 5.2, 18.2, id="float"),
    ],
)
def test_rectangle_area(width, height, area):
    figure = Rectangle(width, height)
    act_area = round(figure.area, 2)

    assert act_area == area, (
        f"Площадь равна {act_area}, ожидаемый результат = {area}"
    )


@pytest.mark.regression
@pytest.mark.parametrize(
    ("width", "height", "perimeter"),
    [
        pytest.param(3, 5, 16, marks=pytest.mark.smoke, id="int"),
        pytest.param(3.5, 5.2, 17.4, id="float"),
    ],
)
def test_rectangle_perimeter(width, height, perimeter):
    figure = Rectangle(width, height)
    act_perimeter = round(figure.perimeter, 2)

    assert act_perimeter == perimeter, (
        f"Периметр равен {act_perimeter}, ожидаемый результат {perimeter}"
    )



