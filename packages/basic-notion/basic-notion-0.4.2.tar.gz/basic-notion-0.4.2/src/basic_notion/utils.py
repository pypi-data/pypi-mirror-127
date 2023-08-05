from typing import Any


def get_from_dict(dct: dict, key: tuple[str, ...]) -> Any:
    data: Any = dct
    for part in key:
        assert isinstance(data, dict)
        data = data[part]
    return data


def set_to_dict(dct: dict, key: tuple[str, ...], value: Any) -> None:
    data = dct
    *parts, last_part = key
    for part in parts:
        if part not in data:
            data[part] = {}
        new_data = data[part]
        data = new_data

    data[last_part] = value


def del_from_dict(dct: dict, key: tuple[str, ...]) -> None:
    data = dct
    *parts, last_part = key
    for part in parts:
        if part not in data:
            data[part] = {}
        new_data = data[part]
        data = new_data

    if last_part in data:
        del data[last_part]
