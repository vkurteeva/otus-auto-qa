import pytest
from src.circle import Circle


@pytest.mark.regression
@pytest.mark.parametrize(
    ("radius", "area"),
    [
        pytest.param(3, 28.27, marks=pytest.mark.smoke, id="int"),
        pytest.param(2.5, 19.63, id="float"),
    ],
)
def test_circle_area(radius, area):
    figure = Circle(radius)
    act_area = round(figure.area, 2)

    assert act_area == area, (
        f"Площадь равна {act_area}, ожидаемый результат = {area}"
    )


@pytest.mark.regression
@pytest.mark.regression
@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [
        pytest.param(3, 18.85, marks=pytest.mark.smoke, id="int"),
        pytest.param(2.5, 15.71, id="float"),
    ],
)
def test_circle_perimeter(radius, perimeter ):
    figure = Circle(radius)
    act_perimeter = round(figure.perimeter, 2)

    assert act_perimeter == perimeter, (
        f"Периметр равен {act_perimeter}, ожидаемый результат {perimeter}"
    )



