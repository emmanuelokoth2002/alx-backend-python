#!/usr/bin/env python3
"""Calculate the sum of a list of floats."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list (List[float]): The list of floats to be summed.

    Returns:
        float: The sum of the input list as a float.
    """
    return sum(input_list)
