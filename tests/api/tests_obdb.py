import pytest


def test_get_list_without_filters(api_client):
    res = api_client.get_list()

    assert len(res.root) == 50, (
        f"Ошибка: ожидалось 50 объектов, получено {len(res.root)}"
    )


@pytest.mark.parametrize(
    "per_page_val, exp_length",
    [
        pytest.param(None, 50, id="default_without_param"),
        pytest.param(1, 1, id="min_boundary_1"),
        pytest.param(49, 49, id="below_default_49"),
        pytest.param(50, 50, id="exact_default_50"),
        pytest.param(51, 51, id="above_default_51"),
        pytest.param(199, 199, id="below_max_199"),
        pytest.param(200, 200, id="max_boundary_200"),
    ],
)
def test_get_list_valid_per_page(api_client, per_page_val, exp_length):
    res = api_client.get_list(per_page=per_page_val)

    assert len(res.root) == exp_length, (
        f"Ошибка: ожидалось {exp_length} объекта(ов), получено {len(res.root)}"
    )


@pytest.mark.parametrize(
    "per_page_val",
    [
        pytest.param(0, id="zero_value"),
        pytest.param("", id="empty_string"),
        pytest.param("abc", id="string_instead_of_int"),
        pytest.param(-10, id="negative_value"),
    ],
)
def test_get_list_invalid_per_page(api_client, per_page_val):
    with pytest.raises(Exception) as exc_info:
        api_client.get_list(per_page="")

    error_text = str(exc_info.value)

    assert "openbrewerydb.org/mcp" in error_text, (
        f"Ошибка: отсутствует ссылка на эндпоинт mcp {error_text}"
    )
    assert "Welcome to" in error_text, (
        f"Ошибка: отсутствует фраза приветствия в ответе {error_text}"
    )


@pytest.mark.parametrize(
    "invalid_filters",
    [
        pytest.param({"by_city": "Fake City"}, id="empty_by_city"),
        pytest.param({"by_state": "Fake State"}, id="empty_by_state"),
        pytest.param({"by_type": "Fake Brewery Type"}, id="empty_type"),
        pytest.param(
            {"by_type": "Fake Brewery Type", "by_city": "Kronach"},
            id="empty_combination",
        ),
        pytest.param({"by_name": "Fake Brewery Name"}, id="empty_by_name"),
    ],
)
def test_get_list_filters_return_empty_list(api_client, invalid_filters):
    res = api_client.get_list(invalid_filters)

    assert isinstance(res.root, list), "Ошибка: ответ API должен быть списком"
    assert len(res.root) == 0, (
        f"Ошибка: ожидался пустой список для фильтров {invalid_filters}, но вернулось объектов: {len(res.root)}"
    )


@pytest.mark.parametrize(
    "filter_param, exp_field, exp_val",
    [
        pytest.param({"by_city": "San Diego"}, "city", "San Diego", id="match_city"),
        pytest.param(
            {"by_country": "United States"},
            "country",
            "United States",
            id="match_country",
        ),
        pytest.param({"by_name": "dog"}, "name", "dog", id="match_name_substring"),
        pytest.param(
            {"by_state": "California"}, "state_province", "California", id="match_state"
        ),
        pytest.param({"by_postal": "92101"}, "postal_code", "92101", id="match_postal"),
        pytest.param({"by_type": "micro"}, "brewery_type", "micro", id="match_type"),
    ],
)
def test_get_list_filters_by_existing_values(
    api_client, filter_param, exp_field, exp_val
):
    res = api_client.get_list(**filter_param)

    assert len(res.root) > 0, (
        f"Ошибка: ожидался хотя бы 1 объект, получено {len(res.root)}"
    )

    for brewery in res.root:
        act_val = getattr(brewery, exp_field)
        assert act_val is not None, (
            f"Ошибка: поле фильтрации отсутствует в ответе {res.root}"
        )
        assert exp_val.lower() in act_val.lower(), (
            f"Ошибка: не совпадает значение в поле фильтрации {res.root}"
        )
