from src.triangle import Triangle
import pytest


@pytest.mark.regression
@pytest.mark.parametrize(
    ("base", "height", "area"),
    [
        pytest.param(3, 4, 6, marks=pytest.mark.smoke, id="int"),
        pytest.param(2.5, 3.5, 4.38, id="float"),
    ],
)
def test_triangle_area(base, height, area):
    figure = Triangle(base, height=height)
    act_area = round(figure.area, 2)

    assert act_area == area, (
        f"Площадь равна {figure.area}, ожидаемый результат = {area}"
    )


@pytest.mark.regression
@pytest.mark.regression
@pytest.mark.parametrize(
    ("base", "leg_a", "leg_b", "perimeter"),
    [
        pytest.param(3, 5, 6, 14, marks=pytest.mark.smoke, id="int"),
        pytest.param(2.5, 4.5, 5.5, 12.5, id="float"),
    ],
)
def test_triangle_perimeter(base, leg_a, leg_b, perimeter ):
    figure = Triangle(base, leg_a, leg_b)
    act_perimeter = round(figure.perimeter, 2)

    assert act_perimeter == perimeter, (
        f"Периметр равен {act_perimeter}, ожидаемый результат {perimeter}"
    )



