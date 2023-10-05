#!/usr/bin/env python3
"""Use mypy to validate the code"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    zoomed_in: Tuple[int] = (
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
