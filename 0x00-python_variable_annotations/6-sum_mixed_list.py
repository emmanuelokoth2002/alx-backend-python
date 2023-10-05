#!/usr/bin/env python3
"""Calculate the sum of a list of integers and floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to be summed.

    Returns:
        float: The sum of the input list as a float.
    """
    return sum(mxd_lst)
