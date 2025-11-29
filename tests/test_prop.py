from functasticpy.pipe import pipe
from functasticpy.prop import prop


def test_prop__basic_usage() -> None:
    get_name = prop("name")

    result = get_name({"name": "Alice", "age": 30})
    assert result == "Alice"


def test_prop__missing_key() -> None:
    get_email = prop("email")

    result = get_email({"name": "Alice", "age": 30})
    assert result is None


def test_prop__with_none() -> None:
    get_name = prop("name")

    result = get_name(None)
    assert result is None


def test_prop__nested_dict() -> None:
    get_city = prop("city")

    result = get_city({"name": "Alice", "city": "NYC", "age": 30})
    assert result == "NYC"


def test_prop__with_different_types() -> None:
    get_count = prop("count")

    result = get_count({"count": 42, "name": "test"})
    assert result == 42

    result = get_count({"count": 0})
    assert result == 0

    result = get_count({"count": False})
    assert result is False


def test_prop__empty_dict() -> None:
    get_name = prop("name")

    result = get_name({})
    assert result is None


def test_prop__in_pipe() -> None:
    result = pipe({"name": "Bob", "age": 25}, prop("name"))
    assert result == "Bob"


def test_prop__with_complex_keys() -> None:
    get_value = prop(("nested", "key"))

    result = get_value({("nested", "key"): "value"})
    assert result == "value"


def test_prop__preserves_none_values() -> None:
    get_value = prop("value")

    result = get_value({"value": None})
    assert result is None
