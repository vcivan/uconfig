from collections.abc import Sequence
from enum import Enum
from typing import Union


NoneType = type(None)

DEFAULT_JSON_INDENT = 2

ALLOWED_BASE_TYPES = [bool, int, float, str, NoneType, Enum]
ALLOWED_CONTAINER_TYPES = [list, dict]


def check_values_are_only_allowed_types(config_dictionary_values: Sequence) -> bool:
    check_is_ok = True
    for value in config_dictionary_values:
        if isinstance(value, dict):
            check_is_ok = check_values_are_only_allowed_types(value.values())
            if not check_is_ok:
                break
        elif isinstance(value, list):
            check_is_ok = check_values_are_only_allowed_types(value)
            if not check_is_ok:
                break
        elif isinstance(value, Enum):
            check_is_ok = all([t in ALLOWED_BASE_TYPES for t in type(value).__mro__[1:-1]])
            if not check_is_ok:
                break
        else:
            check_is_ok = type(value) in ALLOWED_BASE_TYPES
            if not check_is_ok:
                break

    return check_is_ok


def convert_tuples_in_seq_to_lists(sequence: Union[list, tuple]) -> list:
    new_sequence = []
    for item in sequence:
        if isinstance(item, dict):
            new_sequence.append(convert_tuples_in_dict_to_lists(item))
        elif isinstance(item, list) or isinstance(item, tuple):
            new_sequence.append(convert_tuples_in_seq_to_lists(item))
        else:
            new_sequence.append(item)

    return new_sequence

def convert_tuples_in_dict_to_lists(config_dictionary: dict) -> dict:
    new_dict = {}
    for k, v in config_dictionary.items():
        if isinstance(v, dict):
            new_dict[k] = convert_tuples_in_dict_to_lists(v)
        elif isinstance(v, list) or isinstance(v, tuple):
            new_dict[k] = convert_tuples_in_seq_to_lists(v)
        else:
            new_dict[k] = v

    return new_dict


def convert_enums_in_seq_to_values(sequence: Union[list, tuple]) -> Union[list, tuple]:
    sequence_cls = type(sequence)
    new_sequence = []
    for item in sequence:
        if isinstance(item, Enum):
            new_sequence.append(item.value)
        elif isinstance(item, dict):
            new_sequence.append(convert_enums_in_dict_to_values(item))
        elif isinstance(item, list) or isinstance(item, tuple):
            new_sequence.append(convert_enums_in_seq_to_values(item))
        else:
            new_sequence.append(item)

    return sequence_cls(new_sequence)



def convert_enums_in_dict_to_values(config_dictionary: dict) -> dict:
    new_dict = {}
    for k, v in config_dictionary.items():
        if isinstance(v, Enum):
            new_dict[k] = v.value
        elif isinstance(v, dict):
            new_dict[k] = convert_enums_in_dict_to_values(v)
        elif isinstance(v, list) or isinstance(v, tuple):
            new_dict[k] = convert_enums_in_seq_to_values(v)
        else:
            new_dict[k] = v

    return new_dict
