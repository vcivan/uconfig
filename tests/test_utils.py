from uconfig.examples.example_configs import UserTypes, AppId
from uconfig.utils import (
    check_values_are_only_allowed_types,
    convert_tuples_in_dict_to_lists,
    convert_enums_in_dict_to_values
)


good_config1 = {
    "dictionary": {
        "a": 1234,
        "b": "some random string",
        "c": [1, 2, 3, 4],
        "d": {
            "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
            "b": "another random string"
        },
        "e": True,
        "f": None,
        "g": AppId.VENDOR_APP,
        "h": [[1, 2], [3, 4]]
    },
    "list": ["a", "bc", "def", AppId.CLIENT_APP],
    "bool": False,
    "int": 6,
    "float": 7.6,
    "str": "a third random strin",
    "enum": UserTypes.CLIENT,
}
bad_config1 = {
    "dictionary": {
        "a": 1234,
        "b": "some random string",
        "c": [1, 2, 3, 4],
        "d": {
            "a": (1.1, 2.2, 3.3, UserTypes.VENDOR),
            "b": "another random string"
        },
        "e": True,
        "f": None,
        "g": AppId.VENDOR_APP,
        "h": [[1, 2], [3, 4]]
    },
    "list": ("a", "bc", "def", AppId.CLIENT_APP),
    "bool": False,
    "int": 6,
    "float": 7.6,
    "str": "a third random strin",
    "enum": UserTypes.CLIENT
}
good_config2 = {
    "dictionary": {
        "a": 1234,
        "b": "some random string",
        "c": [1, 2, 3, 4],
        "d": {
            "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
            "b": "another random string"
        },
        "e": True,
        "f": None,
        "g": AppId.VENDOR_APP,
        "h": [[1, 2], [3, 4]],
        "i": [[1, 2], [3, 4]],
        "j": [[1, 2], [3, 4]]
    },
    "list": ["a", "bc", "def", AppId.CLIENT_APP],
    "bool": False,
    "int": 6,
    "float": 7.6,
    "str": "a third random strin",
    "enum": UserTypes.CLIENT
}
bad_config2 = {
    "dictionary": {
        "a": 1234,
        "b": "some random string",
        "c": (1, 2, 3, 4),
        "d": {
            "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
            "b": "another random string"
        },
        "e": True,
        "f": None,
        "g": AppId.VENDOR_APP,
        "h": [(1, 2), [3, 4]],
        "i": ([1, 2], [3, 4]),
        "j": ([1, 2], (3, 4))
    },
    "list": ["a", "bc", "def", AppId.CLIENT_APP],
    "bool": False,
    "int": 6,
    "float": 7.6,
    "str": "a third random strin",
    "enum": UserTypes.CLIENT
}


def test_check_are_only_allowed_types_false1():
    assert not check_values_are_only_allowed_types(bad_config1.values())


def test_check_are_only_allowed_types_false2():
    assert not check_values_are_only_allowed_types(bad_config2.values())


def test_check_values_are_only_allowed_types_true1():
    assert check_values_are_only_allowed_types(good_config1.values())


def test_check_values_are_only_allowed_types_true2():
    assert check_values_are_only_allowed_types(good_config2.values())


def test_convert_tuples_in_dict_to_lists1():
    assert good_config1 == convert_tuples_in_dict_to_lists(bad_config1)


def test_convert_tuples_in_dict_to_lists2():
    assert good_config2 == convert_tuples_in_dict_to_lists(bad_config2)


def test_convert_enums_in_dict_to_values():
    converted_dict = convert_enums_in_dict_to_values(good_config1)
    type1 = isinstance(converted_dict["dictionary"]["d"]["a"][3], str)
    type2 = isinstance(converted_dict["dictionary"]["g"], int)
    type3 = isinstance(converted_dict["list"][3], int)
    type4 = isinstance(converted_dict["enum"], str)

    assert type1 and type2 and type3 and type4