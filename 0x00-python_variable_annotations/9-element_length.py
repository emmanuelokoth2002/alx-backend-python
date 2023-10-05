#!/usr/bin/env python3
"""Calculate the length of each element in the input list of sequences."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input
        and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
