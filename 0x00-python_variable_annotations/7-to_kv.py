#!/usr/bin/env python3
"""Create a tuple with the input string and the square of the input integer or float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the input string and the square of the input integer or float.
    """
    return (k, v ** 2)
