import pytest
from urllib.parse import urlparse

from api_handlers.dogs_client import ApiDogsTest as Api


def test_get_list_all_breeds():
    res = Api().get_list_all()

    assert len(res.message) > 0, "Ошибка: вернулся пустой список пород"
    assert res.status == "success", (
        f"Ошибка: вместо status = success, получили status = {res.status}"
    )


@pytest.mark.parametrize("count", [None, 1, 3])
def test_get_random_image(count):
    res = Api().get_random_image(count=count)

    assert res.status == "success", (
        f"Ошибка: вместо status = success, получили status = {res.status}"
    )

    if isinstance(res.message, list):
        urls = [str(url) for url in res.message]
    else:
        urls = [str(res.message)]

    for url in urls:
        assert urlparse(url).netloc == "images.dog.ceo", (
            f"Ошибка: вместо домена 'images.dog.ceo', получили в ссылке '{urlparse(url).netloc}'"
        )

    if count is None:
        assert not isinstance(res.message, list), (
            "Ошибка: вместо одной ссылки, вернулся список"
        )
    else:
        assert len(res.message) == count, (
            f"Ошибка: количество ссылок {len(res.message)} не соответствует запросу {count}"
        )


@pytest.mark.parametrize(
    "breed, count",
    [
        pytest.param("labrador", None, id="get random by breed image"),
        pytest.param("hound", 1, id="get 1 random by breed image"),
        pytest.param("affenpinscher", 3, id="get 2 random by breed images"),
    ],
)
def test_get_random_image_by_breed(breed, count):
    res = Api().get_random_image_by_breed(breed=breed, count=count)

    assert res.status == "success", (
        f"Ошибка: вместо status = success, получили status = {res.status}"
    )

    if isinstance(res.message, list):
        urls = [str(url) for url in res.message]
    else:
        urls = [str(res.message)]

    for url in urls:
        assert urlparse(url).netloc == "images.dog.ceo", (
            f"Ошибка: вместо домена 'images.dog.ceo', получили в ссылке '{urlparse(url).netloc}'"
        )

    if count is None:
        assert not isinstance(res.message, list), (
            "Ошибка: вместо одной ссылки, вернулся список"
        )
    else:
        assert len(res.message) == count, (
            f"Ошибка: количество ссылок {len(res.message)} не соответствует запросу {count}"
        )
