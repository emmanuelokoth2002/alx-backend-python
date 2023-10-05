#!/usr/bin/env python3
"""
Create and return a function that multiplies a float by the given
multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the result of multiplication.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
