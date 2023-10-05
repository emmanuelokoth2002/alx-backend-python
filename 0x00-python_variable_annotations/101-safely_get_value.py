#!/usr/bin/env python3
"""
Safely get a value from a dictionary, with an optional default.
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)
-> Union[Any, T]:
    """
    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to return if
        the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key, or the default
        value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
